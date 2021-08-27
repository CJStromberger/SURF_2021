import math
from field import Field
# for plotting turtlebot locations
import matplotlib.pyplot as plt
import numpy as np

moves = ['pivot CW']

#turtlebot's location
turtlex = []
turtley = []
#turtlebot starting spot
startx = 1
starty = 1
#goal spot
flagx = 3
flagy = 2

turtlex.append(startx)
turtley.append(starty)

f = Field(startx, starty, 0, flagx, flagy)

for move in moves:
    if move == 'push':
        f.push()
        turtlex.append(f.getTurtx())
        turtley.append(f.getTurty())
    elif move == 'pivot CW':
        f.pivotCW()
        turtlex.append(f.getTurtx())
        turtley.append(f.getTurty())
    else:
        f.pivotCCW()
        turtlex.append(f.getTurtx())
        turtley.append(f.getTurty())

# see the turtebot path
fig, ax = plt.subplots()
plt.xlim(0,2)
plt.ylim(0,2)
ax.set_aspect('equal') # make axis same scale
ax.plot(turtlex, turtley, 'r', startx, starty, 'bs', flagx, flagy, 'g^')  # plot path as red dashed line, goal as green line, 
plt.show() # without this it doesn't show up
