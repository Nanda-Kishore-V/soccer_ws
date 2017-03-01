#!/usr/bin/env python
import pygame
import math
import time

pygame.init()

#A:0 B:1 X:2 Y:3
#Axes:
#0&1=>left analog 3&4=>right analog
#LT-2 RT-5
DESP_SHOOT = 0
SHOOT = 1
THRU_BALL = 3
FORWARD_AXIS_LEFT = 0
SIDEWARD_AXIS_LEFT = 1
FORWARD_AXIS_RIGHT = 3
SIDEWARD_AXIS_RIGHT = 4
SPRINT = 5
RT = 5

class Joystick_interface:

    def __init__(self):
        pygame.joystick.init()
        self.count = pygame.joystick.get_count()
        self.angle = 0
        self.omega = True
        if self.count != 0:
            self.joy = pygame.joystick.Joystick(0)
            self.joy.init()
        else:
            self.joy = NULL
            pygame.joystick.quit()
            print "ERROR: No joystick connected."

    #Prints all the values
    def __str__(self):
        string = ""
        for i in xrange(self.joy.get_numaxes()):
            string += "Axis " + str(i) + " : " + str(self.joy.get_axis(i)) + "\n"
        for i in xrange(self.joy.get_numbuttons()):
            string += "Button " + str(i) + " : " + str(self.joy.get_button(i)) + "\n"
        for i in xrange(self.joy.get_numhats()):
            string += "Hat " + str(i) + " : " + str(self.joy.get_hat(i)) + "\n"
        return string

    def __del__(self):
        self.joy.quit()
        pygame.joystick.quit()

    def is_pass(self):
        return self.joy.get_button(PASS)

    def is_shoot(self):
        return self.joy.get_button(SHOOT)

    def get_vel(self):
        return (self.joy.get_axis(FORWARD_AXIS_LEFT),-1*self.joy.get_axis(SIDEWARD_AXIS_LEFT))

    def get_orientation(self):
        if abs(self.joy.get_axis(SIDEWARD_AXIS_RIGHT)) <= 0.1 and abs(self.joy.get_axis(FORWARD_AXIS_RIGHT)) <= 0.1:
            return self.angle
        else:
            self.angle = 180*math.atan2(-1*self.joy.get_axis(SIDEWARD_AXIS_RIGHT),self.joy.get_axis(FORWARD_AXIS_RIGHT))/math.pi
            return self.angle

    def is_run(self):
        return self.joy.get_button(SPRINT)

    def is_thru(self):
        return self.joy.get_button(THRU_BALL)

    def get_omega(self):
        return self.omega

    def set_omega(self,val):
        self.omega = val
        return

    def get_lb(self):
        return self.joy.get_button(5)

    def get_rb(self):
        return self.joy.get_button(4)

    def is_dribble(self):
        if self.joy.get_axis(RT) > 0.5:
            return 1
        else:
            return 0

    def get_desp_shoot(self):
        return self.joy.get_button(DESP_SHOOT)

    def event_get(self):
        pygame.event.get()
