import math
import constants
class Field:
    # Turtle coords
    turtx = 0 
    turty = 0
    turtrad = 0 # orientation of the turtlebot, 0 is pointing right
    # Flag coords
    flagx = 0
    flagy = 0

    def __init__(self, turtle_x, turtle_y, turtle_rad, flag_x, flag_y):
        self.turtx = turtle_x
        self.turty = turtle_y
        self.turtrad = turtle_rad
        self.flagx = flag_x
        self.flagy = flag_y
        self.time = constants.TIME

    # get turtle position and angle
    def getTurtx(self):
        return self.turtx
    def getTurty(self):
        return self.turty
    def getTurtrad(self):
        return self.turtrad

    # get flag positions
    def getFlagx(self):
        return self.flagx
    def getFlagy(self):
        return self.flagy

    # get time
    def getTime(self):
        return self.time
    def setTime(self, new_time):
        self.time = new_time

    # Flag position setting
    def setFlagPos(self, x, y):
        self.flagx = x
        self.flagy = y

    # Turtle position setting functions
    def setTurt(self, x, y, rad):
        self.turtx = x
        self.turty = y
        self.turtrad = rad
    def setTurtPos(self, x, y):
        self.turtx = x
        self.turty = y
    def setTurtAngle(self, rad):
        self.turtrad = rad

    # Pusing functions
    def push(self):
        # changning position
        newx = self.turtx + constants.PUSH_DISTANCE_FORWARD*math.cos(self.turtrad) + constants.PUSH_DISTANCE_TANGENT*math.sin(self.turtrad)
        newy = self.turty + constants.PUSH_DISTANCE_FORWARD*math.sin(self.turtrad) + constants.PUSH_DISTANCE_TANGENT*math.cos(self.turtrad)

        # changing angle
        newrad = self.turtrad + constants.PUSH_RAD

        self.setTurtPos(newx,newy) #setting position
        self.setTurtAngle(newrad) #setting radians
        self.time = self.time - constants.PUSH_TIME #change the time

    # Pivoting clockwise
    def pivotCW(self):
        # turning pushes turtlebot forward
        newx = self.turtx + constants.PIVOTCW_FORWARD*math.cos(self.turtrad) + constants.PIVOTCW_TANGENT*math.sin(self.turtrad)
        newy = self.turty + constants.PIVOTCW_FORWARD*math.sin(self.turtrad) + constants.PIVOTCW_TANGENT*math.cos(self.turtrad)

        # changing angle
        newrad = self.turtrad + constants.PIVOTCW_RAD
        
        # update position, angle and time
        self.setTurtPos(newx,newy)
        self.setTurtAngle(newrad)
        self.time = self.time - constants.PIVOT_TIME

    # Pivoting counterclockwise
    def pivotCCW(self):
        # turning pushes turtlebot forward
        newx = self.turtx + constants.PIVOTCCW_FORWARD*math.cos(self.turtrad) + constants.PIVOTCCW_TANGENT*math.sin(self.turtrad)
        newy = self.turty + constants.PIVOTCCW_FORWARD*math.sin(self.turtrad) + constants.PIVOTCCW_TANGENT*math.cos(self.turtrad)

        # changing angle
        newrad = self.turtrad + constants.PIVOTCCW_RAD
        
        # update position, angle and time
        self.setTurtPos(newx,newy)
        self.setTurtAngle(newrad)
        self.time = self.time - constants.PIVOT_TIME

    def distanceFromFlag(self):
        return math.sqrt(pow(abs(self.turtx-self.flagx),2)+pow(abs(self.turty-self.flagy),2))
