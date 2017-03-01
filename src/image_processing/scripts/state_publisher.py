#!/usr/bin/env python
import ip_module
import numpy as np
import rospy
from image_processing.msg import ball
from image_processing.msg import ball_predict
from image_processing.msg import bot_state

SOFT_LIMIT_POSITIVE = 700
SOFT_LIMIT_NEGATIVE = 400

if __name__=="__main__":
    try:
        ball_object = ip_module.Ball()
        flag = 0
        state_publisher = rospy.Publisher('bot_states',bot_state,queue_size=1)
        ball_state_publisher = rospy.Publisher('ball_state',ball,queue_size=1)
        ball_prediction_publisher = rospy.Publisher('ball_predicts',ball_predict,queue_size=1)
        rospy.init_node('state_publisher',anonymous=True)
        rate = rospy.Rate(ball_object.fps)
        centroid = (0,0)
        centroid_small = (0,0)

        while not rospy.is_shutdown():
            original_image = ball_object.get_image()
            image = ball_object.perspective_transform(original_image,ball_object.pts_in_img,ball_object.pts_reqd)

            imageGray = ball_object.rgb2gray(image)
            ret,thresh = ball_object.threshold_image(imageGray,250,255)
            # if not ball_object.display_image(thresh,"thresh"):
            #     flag = 1
            #     break
            contours,hierarchy = ball_object.find_contours(thresh)

            for i in range(len(contours)):
                area = ball_object.find_area(contours[i])
                # print i,area
                if area > 3300 and area < 4700:
                    centroid = ball_object.get_center(contours[i])

                    if centroid != -1:
                        _,thresh = ball_object.threshold_image(imageGray,220,255)
                        cropped_image = ball_object.crop_image(thresh, centroid, 40)

                        if isinstance(cropped_image,int):
                            print "The bot is out of bounds."
                            continue

                        cropped_contours,cropped_hierarchy = ball_object.find_contours(cropped_image)

                        count = 0
                        for j in range(len(cropped_contours)):
                            area_small = ball_object.find_area(cropped_contours[j])

                            if cropped_hierarchy[0][j][2] == -1 and cropped_hierarchy[0][j][3] != -1:
                                count += 1

                                if area_small > 350 and area_small < 600:
                                    centroid_small = ball_object.get_center(cropped_contours[j])

                        yaw_angle = ball_object.get_yaw_angle(40,40,centroid_small[0],centroid_small[1])
                        # print "State: ", centroid[0],centroid[1],yaw_angle
                        # print "Count: ",count
                        bot_msg = bot_state()
                        bot_msg.num_circles = count
                        bot_msg.pose.x = centroid[0]
                        bot_msg.pose.y = centroid[1]
                        bot_msg.pose.theta = -1*yaw_angle
                        # bot_msg.pose.theta = 120
                        rospy.loginfo(bot_msg)
                        state_publisher.publish(bot_msg)

            hsv_image = ball_object.rgb2hsv(image)
            mask_ball = ball_object.get_hsv_mask(hsv_image,ball_object.lower_ball,ball_object.upper_ball)
            contours_ball,hierarchy = ball_object.find_contours(mask_ball)

            for i in range(len(contours_ball)):
                area = ball_object.find_area(contours_ball[i])
                # print i,area
                if area > 60:
                    centroid_ball = ball_object.get_center(contours_ball[i])
                    if centroid_ball == -1:
                        break
                    ball_object.update_state(centroid_ball[0],centroid_ball[1])
                    print (ball_object.cx,ball_object.cy),ball_object.get_velocity()
                    if ball_object.abs_vel() > 10:
                        ball_object.draw_arrow(image)

                # imaginary lines
                ball_object.prediction_lines(image)

                ball_msg = ball()
                ball_msg.x = ball_object.cx
                ball_msg.y = ball_object.cy
                ball_msg.vx = ball_object.vx_pixel
                ball_msg.vy = ball_object.vy_pixel
                rospy.loginfo(ball_msg)
                ball_state_publisher.publish(ball_msg)

                msg = ball_predict()
                # print ball_object.get_prediction(image)
                destination = ball_object.get_prediction(image)
                print destination
                if destination == -1:
                     msg.predicted_x = -1
                     msg.predicted_y = -1
                elif (((ball_msg.vx**(2) + ball_msg.vy**(2))**(0.5)) < 50):
                    if ((ball_msg.vx > 0 and ball_msg.x > SOFT_LIMIT_POSITIVE) or (ball_msg.vx < 0 and ball_msg.y < SOFT_LIMIT_NEGATIVE)) and (((ball_msg.vx**(2) + ball_msg.vy**(2))**(0.5)) > 15):
                        msg.predicted_x = destination[0]
                        msg.predicted_y = destination[1]
                    else:
                        msg.predicted_x = -1
                        msg.predicted_y = -1
                else:
                    msg.predicted_x = destination[0]
                    msg.predicted_y = destination[1]

                ball_prediction_publisher.publish(msg)
                rospy.loginfo(msg)

            if not ball_object.display_image(image):
                flag = 1
                break

            rate.sleep()

            if flag == 1:
                    break
    except rospy.ROSInterruptException:
        pass
