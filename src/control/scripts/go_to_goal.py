#!/usr/bin/env python
import robot
import time
import rospy
import math
from image_processing.msg import ball
from image_processing.msg import bot_state
from image_processing.msg import ball_predict

# IP_ADDR = "192.168.1.102"
IP_ADDR = "192.168.1.103"
# IP_ADDR = "192.168.1.104"
# IP_ADDR = "192.168.1.105"
PORT_NO = 285

HOME = (1000,310,180)
# HOME = (100,310,0)

def callback_bot(msg):
    if msg.num_circles == 4:
        bot_dictionary[msg.num_circles].update_state((msg.pose.x,msg.pose.y,msg.pose.theta))

def callback_ball(msg):
    # print "        msg                          "
    global destination
    destination = (msg.predicted_x,msg.predicted_y,180)
    # if msg.predicted_x == 1000:
    #     if msg.predicted_y > 160 and msg.predicted_y < 460:
    #         destination = (1000,msg.predicted_y,180)
    #     else:
    #         destination = (1000,310,180)
    # else:
    #     # print "Fuck"
    #     destination = (1000,310,180)

if __name__=="__main__":
    global destination
    destination = (1000,310,180)
    try:
        bot1 = robot.robot((0,0,0),"T1_1",IP_ADDR,PORT_NO)
        bot_dictionary = {2:None,3:None,4:bot1,5:None}
        rospy.init_node('goal_keeper',anonymous=True)
        rospy.Subscriber('bot_states',bot_state,callback_bot)
        rospy.Subscriber('ball_predicts',ball_predict,callback_ball)
        print "Waiting..."
        time.sleep(2)
        print "Executing"
        kp_x = 1.0;     kp_y = 1.7;     kp_theta = 0.30
        kd_x = 0.125;   kd_y = 0.1;     kd_theta = 0
        ki_x = 0.00020; ki_y = 0.00020; ki_theta = 0.0
        old_error_x = 0;    old_error_y = 0;    old_error_theta = 0;
        sum_x = 0;          sum_y = 0;          sum_theta = 0;
        while(1):
            # print "I'm here"
            if destination[0] == 100 or destination[0] == -1 or destination[1] > 460 or destination[1] < 160:
                destination = HOME
            error_x = int(destination[0]-bot1.state[0])
            error_y = int(destination[1]-bot1.state[1])
            error_theta = math.atan2(math.sin(math.pi*(destination[2]-bot1.state[2])/180),math.cos(math.pi*(destination[2]-bot1.state[2])/180))
            print "Errors: ",error_x,error_y,error_theta
            x_dot = kp_x*error_x + kd_x*(error_x-old_error_x) + ki_x*sum_x
            y_dot = kp_y*error_y + kd_y*(error_y-old_error_y) + ki_y*sum_y
            if(abs(error_x) > 30 or abs(error_y) > 30):
                # print "I'm here"
                theta_dot = 0
                old_error_x = error_x;  old_error_y = error_y;
                sum_x += error_x;   sum_y += error_y;
            else:
                x_dot = y_dot = 0
                if abs(error_theta) > (math.pi/4):
                    theta_dot = math.atan2(math.sin(kp_theta*error_theta + kd_theta*(error_theta-old_error_theta) + ki_theta*sum_theta),math.cos(kp_theta*error_theta + kd_theta*(error_theta-old_error_theta) + ki_theta*sum_theta))
                    sum_theta += error_theta
                    old_error_theta = error_theta;
                else:
                    theta_dot = 0

            if x_dot >= 175:
                x_dot = 175
            if y_dot >= 175:
                y_dot = 175
            if x_dot <= -175:
                x_dot = -175
            if y_dot <= -175:
                y_dot = -175
            if theta_dot <= -1.57:
                theta_dot = -1.57
            if theta_dot >= 1.57:
                theta_dot = 1.57

            print "x _dot", x_dot, " y_dot ", y_dot, " theta_dot ",theta_dot
            print "destination ", destination
            bot1.go_to_goal(y_dot,x_dot,theta_dot)

    except rospy.ROSInterruptException:
        pass
