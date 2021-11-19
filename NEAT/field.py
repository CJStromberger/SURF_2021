"""
This class keeps track of the turtlebot's position and orientation, 
as well as the goal's
"""

import math
import constants
class Field:
    # Turtle coords
    turt_x = 0 
    turt_y = 0
    turt_rad = 0 # orientation of the turtlebot, 0 is pointing right
    # Flag coords
    flag_x = 0
    flag_y = 0

    def __init__(self, turtle_x, turtle_y, turtle_rad, flag_x, flag_y):
        self.turt_x = turtle_x
        self.turt_y = turtle_y
        self.turt_rad = turtle_rad
        self.flag_x = flag_x
        self.flag_y = flag_y

    # get turtle position and angle
    def get_turt_x(self):
        return self.turt_x
    def get_turt_y(self):
        return self.turt_y
    def get_turt_rad(self):
        return self.turt_rad

    # get flag positions
    def get_flag_x(self):
        return self.flag_x
    def get_flag_y(self):
        return self.flag_y

    # Flag position setting
    def setFlagPos(self, x, y):
        self.flag_x = x
        self.flag_y = y

    # Turtle position setting functions
    def set_turt(self, x, y, rad):
        self.turt_x = x
        self.turt_y = y
        self.turt_rad = rad
    def set_turt_pos(self, x, y):
        self.turt_x = x
        self.turt_y = y
    def set_turt_angle(self, rad):
        self.turt_rad = rad

    # Pusing functions
    def push(self):
        # changning position
        new_x = self.turt_x + constants.PUSH_DISTANCE_FORWARD*math.cos(self.turt_rad) + constants.PUSH_DISTANCE_TANGENT*math.sin(self.turt_rad)
        new_y = self.turt_y + constants.PUSH_DISTANCE_FORWARD*math.sin(self.turt_rad) + constants.PUSH_DISTANCE_TANGENT*math.cos(self.turt_rad)

        # changing angle
        new_rad = self.turt_rad + constants.PUSH_RAD

        self.set_turt_pos(new_x,new_y) #setting position
        self.set_turt_angle(new_rad) #setting radians

    # Pivoting clockwise
    def pivot_cw(self):
        # turning pushes turtlebot forward
        new_x = self.turt_x + constants.PIVOTCW_FORWARD*math.cos(self.turt_rad) + constants.PIVOTCW_TANGENT*math.sin(self.turt_rad)
        new_y = self.turt_y + constants.PIVOTCW_FORWARD*math.sin(self.turt_rad) + constants.PIVOTCW_TANGENT*math.cos(self.turt_rad)

        # changing angle
        new_rad = self.turt_rad + constants.PIVOTCW_RAD
        
        # update position and angle
        self.set_turt_pos(new_x,new_y)
        self.set_turt_angle(new_rad)

    # Pivoting counterclockwise
    def pivot_ccw(self):
        # turning pushes turtlebot forward
        new_x = self.turt_x + constants.PIVOTCCW_FORWARD*math.cos(self.turt_rad) + constants.PIVOTCCW_TANGENT*math.sin(self.turt_rad)
        new_y = self.turt_y + constants.PIVOTCCW_FORWARD*math.sin(self.turt_rad) + constants.PIVOTCCW_TANGENT*math.cos(self.turt_rad)

        # changing angle
        new_rad = self.turt_rad + constants.PIVOTCCW_RAD
        
        # update position and angle
        self.set_turt_pos(new_x,new_y)
        self.set_turt_angle(new_rad)

    def distance_from_flag(self):
        return math.sqrt(pow(abs(self.turt_x-self.flag_x),2)+pow(abs(self.turt_y-self.flag_y),2))
