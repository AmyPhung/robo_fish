#!/usr/bin/env python3
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np
import cv2


class ImageConverter:
    def __init__(self):
        rospy.init_node('image_converter')

        # initialize the camera and grab a reference to the raw camera capture
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))

        # allow the camera to warmup
        time.sleep(0.1)

        # self.cap = cv2.VideoCapture(0)
        # # Decrease resolution
        # # https://www.codingforentrepreneurs.com/blog/open-cv-python-change-video-resolution-or-scale
        # self.cap.set(3, 640/2)
        # self.cap.set(4, 480/2)

        self.bridge = CvBridge()
        self.image_pub = rospy.Publisher("pi_camera", Image, queue_size=1)

    def run(self):
        # capture frames from the camera
        # format="bgr"
        for frame in self.camera.capture_continuous(self.rawCapture, format="rgb", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array

        	# show the frame
        	# cv2.imshow("Frame", image)
        	# key = cv2.waitKey(1) & 0xFF

            # clear the stream in preparation for the next frame
            self.rawCapture.truncate(0)

        	# # if the `q` key was pressed, break from the loop
        	# if key == ord("q"):
        	# 	break

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # img = frame
            # hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            lower= np.array([240])
            upper = np.array([255])

            mask = cv2.inRange(gray,lower,upper)
            cnts,hie = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(image,cnts,-1,(0,255,0),3)

            # Publish
            image_message = self.bridge.cv2_to_imgmsg(image, encoding="rgb8")
            self.image_pub.publish(image_message)


            # Exit when ROS shuts down
            if rospy.is_shutdown():
                break

            # Capture frame-by-frame
            # ret, frame = self.cap.read()

            # Our operations on the frame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # When everything done, release the capture
        # self.cap.release()

if __name__ == '__main__':
    img_convert = ImageConverter()
    img_convert.run()
