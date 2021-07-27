#!/usr/bin/env python

# imports
import rospy, sys, tf
import moveit_commander
from math import *
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander, PlanningSceneInterface
from moveit_msgs.msg import PlanningScene, ObjectColor
from moveit_msgs.msg import Grasp, GripperTranslation
from moveit_msgs.msg import MoveItErrorCodes
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from tf.transformations import quaternion_from_euler
from copy import deepcopy

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
