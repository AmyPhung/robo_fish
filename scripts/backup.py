#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np
import cv2


class ImageConverter:
    def __init__(self):
        rospy.init_node('image_converter')

        self.cap = cv2.VideoCapture(0)
        # Decrease resolution
        # https://www.codingforentrepreneurs.com/blog/open-cv-python-change-video-resolution-or-scale
        self.cap.set(3, 640/2)
        self.cap.set(4, 480/2)

        self.bridge = CvBridge()
        self.image_pub = rospy.Publisher("pi_camera", Image, queue_size=1)

    def run(self):
        while not rospy.is_shutdown():
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # Our operations on the frame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            image_message = self.bridge.cv2_to_imgmsg(frame, encoding="rgb8")
            self.image_pub.publish(image_message)

            # Display the resulting frame
            # cv2.imshow('frame',gray)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

        # When everything done, release the capture
        self.cap.release()
        # cv2.destroyAllWindows()



#
#
# def talker():
#     pub = rospy.Publisher('chatter', String, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "hello world %s" % rospy.get_time()
#         rospy.loginfo(hello_str)
#         pub.publish(hello_str)
#         rate.sleep()
#
if __name__ == '__main__':
    img_convert = ImageConverter()
    img_convert.run()
