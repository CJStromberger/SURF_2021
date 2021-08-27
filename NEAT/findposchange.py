import math
 
# from https://automaticaddison.com/how-to-convert-a-quaternion-into-euler-angles-in-python/
def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z # in radians


file = 'dataFile.txt'
f = open(file, 'r')

lines = f.readlines() # not the most efficent but it doesn't really matter
nums0 = lines[0].split(' ') #initial positions
numsf = lines[-1].split(' ') #final positions

#intial variables
x0 = float(nums0[0])
y0 = float(nums0[1])
z0 = float(nums0[2])
rot_x0 = float(nums0[4])
rot_y0 = float(nums0[5])
rot_z0 = float(nums0[6])
rot_w0 = float(nums0[7])
(roll_x0, pitch_y0, yaw_z0) = euler_from_quaternion(rot_x0, rot_y0, rot_z0, rot_w0)

#final variables
xf = float(numsf[0])
yf = float(numsf[1])
zf = float(numsf[2])
rot_xf = float(numsf[4])
rot_yf = float(numsf[5])
rot_zf = float(numsf[6])
rot_wf = float(numsf[7])
(roll_xf, pitch_yf, yaw_zf) = euler_from_quaternion(rot_xf, rot_yf, rot_zf, rot_wf)

#differnces
dx = xf - x0
dy = yf - y0
dz = zf - z0
droll_x = roll_xf - roll_x0
dpitch_y = pitch_yf - pitch_y0
dyaw_z = yaw_zf - yaw_z0

# the variables do not match the text bc I need to convert coordinate systems (x in optitrack is y in field and z in optitrack is y in field)
# print("y movement:", dx*3.281, dy*3.281, "x movement:", dz, droll_x, "rads turned:", dpitch_y, dyaw_z) #convert to feet
print("x movement:", (dz * 3.281)*math.cos(pitch_y0) + (dx * 3.281)*math.sin(pitch_y0)) # gotta change axis, I think this works
print("y movement:", (dx * 3.281)*math.cos(pitch_y0) - (dz * 3.281)*math.sin(pitch_y0)) # gotta change axis
print("rads turned:", dpitch_y)
