#!/usr/bin/env python
import joystick
import robot
import time
import math
import rospy
from image_processing.msg import ball
from image_processing.msg import bot_state

IP_ADDR_1 = "192.168.1.102"
PORT_NO_1 = 285
# IP_ADDR_2 = "192.168.43.25"
# PORT_NO_2 = 285
IP_ADDR_3 = "192.168.43.25"
PORT_NO_3 = 285
# IP_ADDR_4 = "192.168.43.25"
# PORT_NO_4 = 285

def callback_bot(msg):
    if msg.num_circles == 2:
        bot_dictionary[msg.num_circles].update_state((msg.pose.x,msg.pose.y,msg.pose.theta))
    # print msg.num_circles,msg.pose.x,msg.pose.y,msg.pose.theta
    # rospy.spin()
    # rospy.loginfo(rospy.get_caller_id() + "bot_" + str(msg.num_circles) + " : " + str((msg.pose.x,msg.pose.y,msg.pose.theta)))

if __name__=="__main__":
    try:
        stick = joystick.Joystick_interface()
        bot1 = robot.robot((0,0,0),"T1_1",IP_ADDR_1,PORT_NO_1)
        # bot2 = robot.robot((0,0,0),"T2_1",IP_ADDR_2,PORT_NO_2)
        # bot3 = robot.robot((0,0,0),"T1_2",IP_ADDR_3,PORT_NO_3)
        # bot4 = robot.robot((0,0,0),"T2_2",IP_ADDR_4,PORT_NO_4)
        bot_dictionary = {2:bot1,3:None,4:None,5:None}
        rospy.init_node('bot_control',anonymous=True)
        rospy.Subscriber('bot_states',bot_state,callback_bot)
        print "Waiting..."
        time.sleep(2)
        print "Exectuting"
        scale_x = 100
        scale_y = 100
        while(1):
            stick.event_get()
            vel = stick.get_vel()
            dest_orientation = stick.get_orientation()
            w = math.atan2(math.sin((dest_orientation - bot1.state[2] - 90)*math.pi/180),math.cos((dest_orientation - bot1.state[2] - 90)*math.pi/180))
            # print w
            # print vel
            bot1.move(scale_x*vel[0],scale_y*vel[1],0)
            # bot1.move(0.1,0.1,0.1)
            # time.sleep(0.05)
            # print bot1.state[2]
        del(stick)
    except rospy.ROSInterruptException:
        pass
