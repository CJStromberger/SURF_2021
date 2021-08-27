
import math
# for plotting turtlebot locations
import matplotlib.pyplot as plt
import numpy as np

file = 'dataFile.txt'
f = open(file, 'r')

#turtlebot's location
turtlex = []
turtley = []
#turtlebot starting spot
startx = 1
starty = 1
#goal spot
flagx = 3
flagy = 2

turtlestart = f.readline().split(' ') #read the initial starting position

offsetx = startx - float(turtlestart[2])*3.281 #put the turtlebot at the starting x position
offsety = starty - float(turtlestart[0])*3.282 #put the turtlebot at the starting y position

counter = 1 # so we dont have to go through every line
for line in f:
    if (counter % 50 == 0):
        pos = line.split(' ')
        turtlex.append(float(pos[2])*3.281 + offsetx)
        turtley.append(float(pos[0])*3.281 + offsety)
    counter += 1

# see the turtebot path
fig, ax = plt.subplots()
plt.xlim(0,4)
plt.ylim(0,4)
ax.set_aspect('equal') # make axis same scale
ax.plot(turtlex, turtley, 'r', startx, starty, 'bs', flagx, flagy, 'g^')  # plot path as red dashed line, goal as green line, 
plt.show() # without this it doesn't show up
