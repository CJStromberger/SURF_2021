#!/usr/bin/env python

'''Copyright (c) 2015, Mark Silliman
All rights reserved.'''
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import sys, select, termios, tty
import time

# Length between wheels, 9 inches, 0.2286 meters
BASE = 0.2286

class GoForward():
    def __init__(self):
        # initiliaze
        rospy.init_node('GoForward', anonymous=False)

	    # tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")

        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
	    # Create a publisher which can "talk" to TurtleBot and tell it to move
        # Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
     
	    #TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
        r = rospy.Rate(5);
        # Twist is a datatype for velocity
        move_cmd = Twist()
	    # let's go forward at 0.2 m/s
        move_cmd.linear.x = 0.2
	    # let's turn at 0 radians/s
        move_cmd.angular.z = 0

	    # as long as you haven't ctrl + c keeping doing...
        while not rospy.is_shutdown():
            for i in range(100):
                speeds = self.fixwheelspeed(-.1, -.1)
                move_cmd.linear.x = speeds[0]
                move_cmd.angular.z = speeds[1]
	            # publish the velocity
                self.cmd_vel.publish(move_cmd)
	            # wait for 0.1 seconds (10 HZ) and publish again
                r.sleep()
                        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
	    # a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.cmd_vel.publish(Twist())
	    # sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)
    
    # Takes a desired velocity of the left wheel and right wheel and returns a (linear velocity, rortational velocity) tuple
    def fixwheelspeed(self, vleft, vright):
        if vleft == vright:
            return(vleft, 0)
        elif vleft < vright:
            omega = abs(vleft - vright)/BASE
            velocity  = (vleft+vright)/2
            return(velocity, omega)
        else:
            omega = abs(vleft - vright)/BASE
            velocity  = (vleft+vright)/2
            return(velocity, -omega)
 
if __name__ == '__main__':
    try:
        print("sleeping")
        time.sleep(4)
        print("going")
        time.sleep(1)
        GoForward()
    except:
        rospy.loginfo("GoForward node terminated.")
