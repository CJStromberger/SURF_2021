#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def talker():
    pub_wrist = rospy.Publisher('/arm_wrist_flex_joint/command', Float64, queue_size=10)
    pub_pan = rospy.Publisher('/arm_shoulder_pan_joint/command', Float64, queue_size=10)
    pub_shoulder = rospy.Publisher('/arm_shoulder_lift_joint/command', Float64, queue_size=10)
    pub_elbow = rospy.Publisher('/arm_elbow_flex_joint/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.5) # 0.5 hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        pub_wrist.publish(-math.pi/2)
        pub_elbow.publish(-math.pi/3)
        pub_shoulder.publish(math.pi/2)
        pub_pan.publish(math.pi/5)
        rate.sleep()
        pub_pan.publish(-math.pi/5)
        rate.sleep()
        pub_pan.publish(0)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
