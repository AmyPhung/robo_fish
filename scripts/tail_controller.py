#!/usr/bin/env python3
import time
import rospy
from std_msgs.msg import Int16
import RPi.GPIO as GPIO

class TailController:
    def __init__(self):

        rospy.init_node('tail_controller')

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.pwm = GPIO.PWM(18, 100)
        self.pwm.start(5)

        self.cmd_sub = rospy.Subscriber("servo_cmd", Int16, self.servoCmdCB)
        rospy.loginfo("tail_controller node initialized")

    def servoCmdCB(self, msg):
        # TODO: add rate limiting to this
        angle_cmd = msg.data

        # Limit angle range
        if angle_cmd < 0:
            angle_cmd = 0
        elif angle_cmd > 180:
            angle_cmd = 180

        rospy.loginfo("Setting servo angle to %2d", angle_cmd)
        # Update servo position
        duty = float(angle_cmd) / 10.0 + 2.5
        self.pwm.ChangeDutyCycle(duty)
        rospy.loginfo("Using duty cycle %5.1f", duty)

    def run(self):
        while not rospy.is_shutdown():
            pass

if __name__ == '__main__':
    tail_controller = TailController()
    tail_controller.run()
