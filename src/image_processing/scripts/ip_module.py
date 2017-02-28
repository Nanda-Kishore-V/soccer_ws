#!/usr/bin/env python
import cv2
import numpy as np
import math
import time

FULL_WIDTH = 1920
FULL_HEIGHT = 1080

FINAL_WIDTH  = 1100
FINAL_HEIGHT = 620

LEFT_TOP = [94,14]
RIGHT_TOP = [1714,152]
RIGHT_BOTTOM = [1670,1054]
LEFT_BOTTOM = [36,1034]

class IP(object):

    def __init__(self):
        self.cap = cv2.VideoCapture(1)
        self.cap.set(3,FULL_WIDTH) #3 - WIDTH
        self.cap.set(4,FULL_HEIGHT)  #4 - HEIGHT

    def get_image(self):
        ret,image = self.cap.read()
        # print image
        while not np.size(image,0) == FULL_HEIGHT or not np.size(image,1) == FULL_WIDTH:
            print "trying"
            ret,image = self.cap.read()
        return image

    def perspective_transform(self,image,pts1,pts2):
        return cv2.warpPerspective(image,cv2.getPerspectiveTransform(pts1,pts2),(FINAL_WIDTH,FINAL_HEIGHT))

    def rgb2gray(self,image):
        return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    def rgb2hsv(self,image):
        return cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    def threshold_image(self,image,threshold,max_val):
        return cv2.threshold(image,threshold,max_val,cv2.THRESH_BINARY)

    def display_image(self,image,window_name = "Image"):
        cv2.imshow(window_name,image)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            return 0
        return 1

    def find_contours(self,image):
        major,_,_ = cv2.__version__.split('.')
        if major == '3':
            _,contour,hierarchy = cv2.findContours(image, cv2.RETR_TREE, 2)
        else:
            contour,hierarchy = cv2.findContours(image, cv2.RETR_TREE, 2)
        return contour,hierarchy

    def find_area(self,contour):
        return cv2.contourArea(contour)

    def find_moments(self,contour):
        return cv2.moments(contour)

    def crop_image(self,image,center,amount):
        # if int(center[1])-amount >= 0 and int(center[0])-amount >= 0:
            # if int(center[1])+amount <= 2*amount and int(center[0])+amount <= 2*amount:
        img = image[(int(center[1])-amount):(int(center[1])+amount),(int(center[0])-amount):(int(center[0])+amount)]
        return img
            # else:
            #     return [-1]
        # else:
        #     return [-1]

    def get_hsv_mask(self,image,lower,upper):
        return cv2.inRange(image, lower, upper)

    def end_all(self):
        self.cap.release()
        cv2.destroyAllWindows()


class detectRobot(IP):

    def __init__(self):
        self.pts_in_img = np.float32([LEFT_TOP,RIGHT_TOP,RIGHT_BOTTOM,LEFT_BOTTOM])
        self.pts_reqd = np.float32([[0,0],[FINAL_WIDTH,0],[FINAL_WIDTH,FINAL_HEIGHT],[0,FINAL_HEIGHT]])

        super(detectRobot,self).__init__()

    # Input: image(RGB),threshold
    # Output: Contours and hierarchy in the same order
    def preprocessing(self,image,threshold,displayImage=False):
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray,threshold,255,cv2.THRESH_BINARY)
        if displayImage:
            self.display_image(thresh)
        contour,hierarchy = self.find_contours(thresh)
        return ret,thresh,contour,hierarchy

    def get_center(self,contour):
        M = cv2.moments(contour)
        if M["m00"] == 0:
            return -1
        else:
            return M["m10"]/M["m00"],M["m01"]/M["m00"]

    def get_yaw_angle(self,cX,cY,yX,yY):
        return math.atan2(cY-yY,cX-yX)*180/math.pi

class Ball(detectRobot):

    def __init__(self):
        super(Ball,self).__init__()
        self.fps = 28
        self.update_fps(60)

        self.lower_ball = np.array([23,52,230])
        self.upper_ball = np.array([40,120,260])

        self.vx_pixel = 0;  self.vy_pixel = 0

        self.cx_old = 0;    self.cy_old = 0;
        self.cx = 0;        self.cy = 0
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.sides = [[(100,0),(100,1022)],[(1000,0),(1000,1022)]]

        self.dir = 0;       self.destination = (100,310)

    def update_fps(self,num_frames=120):
        print "Checking fps..."
        print "Capturing {0} frames".format(num_frames)
        # Start time
        start = time.time()
        # Grab a few frames
        for i in xrange(0, num_frames) :
            ret, frame = self.cap.read()
        # End time
        end = time.time()
        # Time elapsed
        seconds = end - start
        print "Time taken : {0} seconds".format(seconds)
        # Calculate frames per second
        fps  = num_frames / seconds;
        print "Estimated frames per second : {0}".format(fps);
        self.fps = fps

    def update_state(self,cx,cy):
        self.cx_old = self.cx
        self.cy_old = self.cy
        self.cx = cx
        self.cy = cy
        self.get_velocity()

    def get_velocity(self):
        self.vx_pixel = int((self.cx-self.cx_old)*self.fps)
        self.vy_pixel = int((self.cy-self.cy_old)*self.fps)
        if self.vx_pixel < 0:
            self.dir = 0
        else:
            self.dir = 1
        return int(self.vx_pixel),int(self.vy_pixel)

    def vector_length(self):
        return int(self.cx+self.vx_pixel), int(self.cy+self.vy_pixel)

    def draw_arrow(self,img):
        cv2.line(img,(int(self.cx),int(self.cy)),self.vector_length() ,(255,255,0),5)
        cv2.putText(img,str((int(self.vx_pixel),int(self.vy_pixel))),(int(self.cx),int(self.cy)), self.font, 0.5,(255,255,0),2,cv2.LINE_AA)

    def prediction_lines(self,img):
        cv2.line(img,self.sides[0][0],self.sides[0][1],(255,0,0),5)
        cv2.line(img,self.sides[1][0],self.sides[1][1],(255,0,0),5)

    def get_prediction(self,image):
        if self.vx_pixel:
            time_to_line = (self.sides[self.dir][0][0] - self.cx)/self.vx_pixel
            dest_y = self.cy + time_to_line*self.vy_pixel
            if dest_y < 0 or dest_y > FINAL_WIDTH:
                return -1
            cv2.circle(image,(int(self.sides[self.dir][0][0]),int(dest_y)), 5, (0,0,255), -1)
            self.destination = self.sides[self.dir][0][0],dest_y
            cv2.putText(image,str(self.destination),(int(self.destination[0]),int(self.destination[1])), self.font, 0.5,(255,255,0),2,cv2.LINE_AA)
        return self.destination

    def abs_vel(self):
        return math.sqrt(self.vx_pixel**2+self.vy_pixel**2)
