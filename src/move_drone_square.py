#!/usr/bin/env python

# Import Needed Packages
import time
import rospy
import actionlib
from actionlib.msg import TestAction, TestFeedback, TestResult
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty


class MoveSquareClass(object):

    # Create Feedback/Result Msgs
    _feedback = TestFeedback()
    _result = TestResult()

    def __init__(self):
        # Create Action Server
        self._as = actionlib.SimpleActionServer('move_drone_square_as', TestAction, self.goal_callback, False)
        self._as.start()
        self.ctrl_c = False
        self.rate = rospy.Rate(10)

    def publish_once_in_cmd_vel(self, cmd):
        while not self.ctrl_c:
            connections = self._pub_cmd_vel.get_num_connections()
            if connections > 0:
                self._pub_cmd_vel.publish(cmd)
                rospy.loginfo("Publish In /cmd_vel...")
                break
            else:
                self.rate.sleep()

    def stop_drone(self):
        rospy.loginfo("Stopping...")
        self._move_msg.linear.x = 0.0
        self._move_msg.angular.z = 0.0
        self.publish_once_in_cmd_vel(self._move_msg)

    def turn_drone(self):
        rospy.loginfo("Turning...")
        self._move_msg.linear.x = 0.0
        self._move_msg.angular.z = 1.0
        self.publish_once_in_cmd_vel(self._move_msg)

    def move_forward(self):
        rospy.loginfo("Moving Forward...")
        self._move_msg.linear.x = 1.0
        self._move_msg.angular.z = 0.0
        self.publish_once_in_cmd_vel(self._move_msg)

    def goal_callback(self, goal):
        # Helper Variables
        r = rospy.Rate(1)
        success = True

        # Define Msgs And Publishers Used
        self._pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self._move_msg = Twist()
        self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self._takeoff_msg = Empty()
        self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)
        self._land_msg = Empty()

        # Drone Takeoff
        i = 0
        while not i == 3:
            self._pub_takeoff.publish(self._takeoff_msg)
            rospy.loginfo('Taking off...')
            time.sleep(1)
            i += 1

        # Define Seconds To Move Along Side (Defined By Goal)
        # And Seconds To Turn
        sideSeconds = goal.goal
        turnSeconds = 1.8

        # Begin Callback Main Functionality
        i = 0
        for i in xrange(0,4):
            # Check Preempt Status
            if self._as.is_preempt_requested():
                rospy.loginfo("The Goal Has Been Cancelled!")
                self._as.set_preempted()
                success = False
                break

            # Drone Logic
            self.move_forward()
            time.sleep(sideSeconds)
            self.turn_drone()
            time.sleep(turnSeconds)

            # Build And Publish Feedback Msg
            self._feedback.feedback = i
            self._as.publish_feedback(self._feedback)
            r.sleep()

        if success:
            self._result.result = (sideSeconds*4) + (turnSeconds*4)
            rospy.loginfo("Total Seconds Taken: %i" % self._result.result)
            self._as.set_succeeded(self._result)

            # Stop And Land Drone
            self.stop_drone()

            i=0
            while not i==3:
                self._pub_land.publish(self._land_msg)
                rospy.loginfo("Landing...")
                time.sleep(1)
                i += 1


if __name__ == '__main__':
    rospy.init_node("move_square")
    MoveSquareClass()
    rospy.spin()