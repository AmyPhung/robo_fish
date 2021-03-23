#!/usr/bin/env python3

import numpy as np
import cv2
import time

class LEDDetector():
    def __init__(self):
        pass

    def checkDetections(self, frame):

        return frame

if __name__=="__main__":
    led_detector = LEDDetector()

    cap = cv2.VideoCapture(0)
    # Decrease resolution
    # https://www.codingforentrepreneurs.com/blog/open-cv-python-change-video-resolution-or-scale
    cap.set(3, 640/2)
    cap.set(4, 480/2)
    # time.sleep(2)


    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # led_detector.checkDetections(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # img = frame
        # hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        lower= np.array([240])
        upper = np.array([255])

        mask = cv2.inRange(gray,lower,upper)
        cnts,hie = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame,cnts,-1,(0,255,0),3)

        cv2.imshow('mask', mask)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
