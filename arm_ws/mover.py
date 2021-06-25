#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64


def talker():

    # Set up for 3 joint arm (Anthropomorphic)
    pan = rospy.Publisher('/head_pan_joint/command', Float64, queue_size=10)
    tilt = rospy.Publisher('/head_tilt_joint/command', Float64, queue_size=10)
    topple = rospy.Publisher('/head_topple_joint/command', Float64, queue_size=10)

    # Make this a node in Ros
    rospy.init_node('mover')

    # The rate at which the messages are sent
    rate = rospy.Rate(70)  # 10hz

    # This will just move it to a position
    # A loop is not needed.
    while not rospy.is_shutdown():

        # Create the end position (in radians)
    pan_pos = -1.0
        tilt_pos = 0.5
        topple_pos = -1.0

        # Log the information to /rosout
    rospy.loginfo(pan_pos)
        rospy.loginfo(tilt_pos)
        rospy.loginfo(topple_pos)

    # Finally, publish to a node
    pan.publish(pan_pos)
        tilt.publish(tilt_pos)
        topple.publish(topple_pos)

    rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
