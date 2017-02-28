#!/usr/bin/env python
import robot
import time
import rospy
import math
from image_processing.msg import ball
from image_processing.msg import bot_state
from image_processing.msg import ball_predict

IP_ADDR_1 = "192.168.1.102"
PORT_NO_1 = 285

def callback_bot(msg):
    if msg.num_circles == 2:
        bot_dictionary[msg.num_circles].update_state((msg.pose.x,msg.pose.y,msg.pose.theta))

def callback_ball(msg):
    global destination
    if msg.predicted_x == 1000:
        destination = (1000,msg.predicted_y)

if __name__=="__main__":
    global destination
    destination = (0,0,0)
    try:
        bot1 = robot.robot((0,0,0),"T1_1",IP_ADDR_1,PORT_NO_1)
        bot_dictionary = {2:bot1,3:None,4:None,5:None}
        rospy.init_node('bot_control',anonymous=True)
        rospy.Subscriber('bot_states',bot_state,callback_bot)
        rospy.Subscriber('ball_predicts',ball_predict,callback_ball)
        print "Waiting..."
        time.sleep(2)
        print "Executing"
        kp_x = 0.9
        kp_y = 0.9
        kp_theta = 0.85
        kd_x = 0.1
        kd_y = 0.1
        kd_theta = 0
        ki_x = 0.00025
        ki_y = 0.00025
        ki_theta = 0.00

        old_error_x = 0;    old_error_y = 0;    old_error_theta = 0;
        sum_x = 0;          sum_y = 0;          sum_theta = 0;
        while(1):
            error_x = int(destination[0]-bot1.state[0])
            error_y = int(destination[1]-bot1.state[1])
            error_theta = math.pi*(destination[2]-bot1.state[2])/180
            print "Errors: ",error_x,error_y,error_theta
            x_dot = kp_x*error_x + kd_x*(error_x-old_error_x) + ki_x*sum_x
            y_dot = kp_y*error_y + kd_y*(error_y-old_error_y) + ki_y*sum_y
            if(abs(error_x) > 40 or abs(error_y) > 40):
                print "I'm here"
                theta_dot = 0
                old_error_x = error_x;  old_error_y = error_y;
                sum_x += error_x;   sum_y += error_y;
            else:
                x_dot = y_dot = 0
                if abs(error_theta) > 0.1:
                    theta_dot = math.atan2(math.sin(kp_theta*error_theta + kd_theta*(error_theta-old_error_theta) + ki_theta*sum_theta),math.cos(kp_theta*error_theta + kd_theta*(error_theta-old_error_theta) + ki_theta*sum_theta))
                    sum_theta += error_theta
                    old_error_theta = error_theta;
                else:
                    theta_dot = 0


            if x_dot >= 250:
                x_dot = 250
            if y_dot >= 250:
                y_dot = 250
            if x_dot <= -250:
                x_dot = -250
            if y_dot <= -250:
                y_dot = -250
            if theta_dot <= -1.57:
                theta_dot = -1.57
            if theta_dot >= 1.57:
                theta_dot = 1.57
            # print "Velocities: ",x_dot,y_dot,theta_dot
            # max_val = max(abs(x_dot),abs(y_dot))
            # if max_val != 0:
            #     x_dot /= max_val*0.01
            #     y_dot /= max_val*0.01
            print "destination", destination 
            print "x_dot ",x_dot,"y_dot ",y_dot," theta_dot ",theta_dot
            bot1.go_to_goal(y_dot,x_dot,theta_dot)
    except rospy.ROSInterruptException:
        pass
