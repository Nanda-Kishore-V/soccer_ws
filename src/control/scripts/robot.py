#!/usr/bin/env python
from __future__ import division
import math
import socket
import rospy

#Required constants
WHEEL_RADIUS = 5   #cm
BOT_RADIUS = 13.5  #cm
MIN_VEL = 30
MIN_VEL_GTG = 90
class robot:

    def __init__(self,init_state,number,ip,port):
        self.state = init_state   #provide from IP
        self.bot_number = number   #give numbers to each robot T1_1 T2_1 etc..
        self.wheel_radius = WHEEL_RADIUS
        self.bot_radius = BOT_RADIUS
        self.tcp_ip = ip;         self.tcp_port = port   #ip address of each robot
        self.buffer_size = 1024

    #Sends message to the ip address mentioned.
    #Returns 1 if success else returns 0
    def send(self,message):
        # print "I'm here"
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.tcp_ip, self.tcp_port))
        self.sock.send(message)
        data = self.sock.recv(self.buffer_size)
        self.sock.close()
        if(data != 'H'):
            print "Error: Incorrect acknowledgement from robot ",self.bot_number
            return 0
        else:
            return 1

    #Finds wheel velocities for given (v_x,v_y,w)
    #Returns 1 if data is sent to robot else returns 0
    def move(self,x_dot,y_dot,w):
        # print "velocities:",(x_dot,y_dot,w)
        vel_w_1 = ((-1*math.sin((30+self.state[2])*math.pi/180)*x_dot) + math.cos((30+self.state[2])*math.pi/180)*y_dot + self.bot_radius*w)/self.wheel_radius;
        vel_w_2 = ((-1*math.sin((-90+self.state[2])*math.pi/180)*x_dot) + math.cos((-90+self.state[2])*math.pi/180)*y_dot + self.bot_radius*w)/self.wheel_radius;
        vel_w_3 = ((-1*math.sin((150+self.state[2])*math.pi/180)*x_dot) + math.cos((150+self.state[2])*math.pi/180)*y_dot + self.bot_radius*w)/self.wheel_radius;
        max_val = max(abs(vel_w_1),abs(vel_w_2),abs(vel_w_3))
        if max_val <= 1:
            vel_w_1 = 0
            vel_w_2 = 0
            vel_w_3 = 0
        elif round(max_val,0) == abs(round(vel_w_1,0)) and round(max_val,0) == abs(round(vel_w_2,0)) and round(max_val,0) == abs(round(vel_w_3,0)):
            # print "I'm here"
            vel_w_1 = (vel_w_1)*(255-60)/10.0
            vel_w_2 = (vel_w_2)*(255-60)/10.0
            vel_w_3 = (vel_w_3)*(255-60)/10.0
            # print "wheel_velocities: ",vel_w_1,vel_w_2,vel_w_3
            if vel_w_1 > 0:
                vel_w_1 += 60
            else:
                vel_w_1 -= 60
            if vel_w_2 > 0:
                vel_w_2 += 60
            else:
                vel_w_2 -= 60
            if vel_w_3 > 0 :
                vel_w_3 += 60
            else:
                vel_w_3 -= 60
        else:
            # print "I'm here too"
            vel_w_1 /= max_val; vel_w_2 /= max_val; vel_w_3 /= max_val;
            vel_w_1 *= (200-MIN_VEL)
            if vel_w_1 > 0:
                vel_w_1 += MIN_VEL
            else:
                vel_w_1 -= MIN_VEL
            vel_w_2 *= (200-MIN_VEL)
            if vel_w_2 > 0:
                vel_w_2 += MIN_VEL
            else:
                vel_w_2 -= MIN_VEL
            vel_w_3 *= (200-MIN_VEL)
            if vel_w_3 > 0 :
                vel_w_3 += MIN_VEL
            else:
                vel_w_3 -= MIN_VEL
        message = str(int(vel_w_1))+":"+str(int(vel_w_2))+":"+str(int(vel_w_3))+";"+"\0"
        print message
        return self.send(message)

    def update_state(self,given_state):
        self.state = given_state;

    def go_to_goal(self,x_dot,y_dot,w):
        vel_w_1 = ((-1*math.sin((30+self.state[2])*math.pi/180)*x_dot) + math.cos((30+self.state[2])*math.pi/180)*y_dot + self.bot_radius*w)/self.wheel_radius;
        vel_w_2 = ((-1*math.sin((-90+self.state[2])*math.pi/180)*x_dot) + math.cos((-90+self.state[2])*math.pi/180)*y_dot + self.bot_radius*w)/self.wheel_radius;
        vel_w_3 = ((-1*math.sin((150+self.state[2])*math.pi/180)*x_dot) + math.cos((150+self.state[2])*math.pi/180)*y_dot + self.bot_radius*w)/self.wheel_radius;
        print "Velocity_wheels:",vel_w_1,vel_w_2,vel_w_3
        max_val = max(abs(vel_w_1),abs(vel_w_2),abs(vel_w_3))
        # print max_val
        if round(max_val,0) == abs(round(vel_w_1,0)) and round(max_val,0) == abs(round(vel_w_2,0)) and round(max_val,0) == abs(round(vel_w_3,0)):
            vel_w_1 = (vel_w_1)*(255-80)/6.0
            vel_w_2 = (vel_w_2)*(255-80)/6.0
            vel_w_3 = (vel_w_3)*(255-80)/6.0
            # print "wheel_velocities: ",vel_w_1,vel_w_2,vel_w_3
            if vel_w_1 > 0:
                vel_w_1 += 80
            else:
                vel_w_1 -= 80
            if vel_w_2 > 0:
                vel_w_2 += 80
            else:
                vel_w_2 -= 80
            if vel_w_3 > 0 :
                vel_w_3 += 80
            else:
                vel_w_3 -= 80

        else:
            # print "I'm here too"
            vel_w_1 /= 70; vel_w_2 /= 70; vel_w_3 /= 70;
            vel_w_1 *= (255-MIN_VEL_GTG)
            if vel_w_1 > 0:
                vel_w_1 += MIN_VEL_GTG
            else:
                vel_w_1 -= MIN_VEL_GTG
            vel_w_2 *= (255-MIN_VEL_GTG)
            if vel_w_2 > 0:
                vel_w_2 += MIN_VEL_GTG
            else:
                vel_w_2 -= MIN_VEL_GTG
            vel_w_3 *= (255-MIN_VEL_GTG)
            if vel_w_3 > 0 :
                vel_w_3 += MIN_VEL_GTG
            else:
                vel_w_3 -= MIN_VEL_GTG
        message = str(int(vel_w_1))+":"+str(int(vel_w_2))+":"+str(int(vel_w_3))+";"+"\0"
        print message
        return self.send(message)
