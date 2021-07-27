#!/usr/bin/env python

# imports
import rospy, sys, tf
import moveit_commander
from math import *
from moveit_commander import MoveGroupCommander, PlanningSceneInterface

GROUP_NAME_ARM = 'arm'

class MoveItDemo:
    def __init__(self):
        
        arm = MoveGroupCommander(GROUP_NAME_ARM)

        rospy.loginfo("Set Arm: right_up")
        arm.set_named_target('right_up')
        if arm.go() != True:
            rospy.logwarn("  Go failed")
        rospy.sleep(2)

if __name__ == "__main__":
    MoveItDemo()
