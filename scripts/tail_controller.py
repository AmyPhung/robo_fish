#!/usr/bin/env python3

# Degree value for center of servo
SERVO_CENTER = 90

# Maximum degree amount below or past center to move
# Important for preventing hardware failures from servo hitting endstops
# and stalling
MAX_SERVO_RANGE = 27

# GPIO Pin to use
SERVO_PIN = 18

# Minimum servo delay for end-to-end sweep (in ms)
MIN_SERVO_DELAY = 500

# For convenience - disables pi-specific code for offboard debugging
OFFBOARD_DEBUG = True

import rospy
from std_msgs.msg import Int16

if not OFFBOARD_DEBUG:
    import pigpio


class TailController:
    def __init__(self):
        # TODO: Add "off mode"

        rospy.init_node('tail_controller')

        if not OFFBOARD_DEBUG:
            # Access raspi pins
            self.pi = pigpio.pi()

        # Default to straight ahead
        self.servo_min_setpoint = 90
        self.servo_max_setpoint = 90
        # Number of milliseconds to wait between movement
        self.servo_delay = 1000

        # Setup subscribers
        self.min_setpoint_sub = rospy.Subscriber("servo_min_setpoint",
            Int16, self.servoMinSetpointCB)
        self.max_setpoint_sub = rospy.Subscriber("servo_max_setpoint",
            Int16, self.servoMaxSetpointCB)
        self.cmd_sub = rospy.Subscriber("servo_delay",
            Int16, self.servoDelayCB)


        rospy.loginfo("tail_controller node initialized")

    def servoMinSetpointCB(self, msg):
        self.servo_min_setpoint = msg.data
        self.servo_min_setpoint = self.checkEndstops(self.servo_min_setpoint)
        rospy.loginfo("Setting minimum servo setpoint to %3d",
            self.servo_min_setpoint)

    def servoMaxSetpointCB(self, msg):
        self.servo_max_range = msg.data
        self.servo_max_setpoint = self.checkEndstops(self.servo_max_setpoint)
        rospy.loginfo("Setting maximum servo setpoint to %3d",
            self.servo_max_setpoint)

    def servoDelayCB(self, msg):
        self.servo_delay = msg.data
        if self.servo_delay < MIN_SERVO_DELAY:
            self.servo_delay  = MIN_SERVO_DELAY
        rospy.loginfo("Setting servo delay to %4d", self.servo_delay)

    def checkEndstops(self, deg_input):
        # Prevent servo from driving past endstops
        if deg_input < SERVO_CENTER - MAX_SERVO_RANGE:
            return SERVO_CENTER - MAX_SERVO_RANGE
        elif deg_input > SERVO_CENTER + MAX_SERVO_RANGE:
            return SERVO_CENTER + MAX_SERVO_RANGE
        else:
            return deg_input

    def intRemap(self, x, in_min, in_max, out_min, out_max):
        """ Takes input x and rescales it to an output range.
        Returns integer values"""
        # Convert everything to floats - necessary for python 2
        x, in_min, in_max, out_min, out_max = \
            float(x), float(in_min), float(in_max), float(out_min), float(out_max)
        return int((x-in_min)/(in_max-in_min)*(out_max-out_min) + out_min)


    def run(self):
        while not rospy.is_shutdown():
            for deg in (self.servo_min_setpoint, self.servo_max_setpoint):
                # Technically shouldn't be necessary, but just in case
                deg = self.checkEndstops(deg)

                # Servo range goes from 0 to 190
                # GPIO Library expects command to be between 1000 and 2000
                pwm = self.intRemap(deg, 0, 180, 1000, 2000)
                print(pwm)

                if not OFFBOARD_DEBUG:
                    self.pi.set_servo_pulsewidth(SERVO_PIN, pwm)

                rospy.sleep(self.servo_delay/1000)

if __name__ == '__main__':
    tail_controller = TailController()
    tail_controller.run()
