"""
This file runs NEAT for the case of dual wheel failure.
"""

# for neuroevolution
import neat #NEAT neuroevolution library
from field import Field #describes the test field/environment
import constants #real values of distances, etc.
import random
import math
# for visualizing the neural network
import visualize 
# for plotting turtlebot locations
import matplotlib.pyplot as plt
import numpy as np

# array of x and y positions in planned path, respectivley
global best_x
global best_y

# locations of the flag and turtlebot
global flag_x
global flag_y
global turt_x
global turt_y

"""
Takes an ouptut from the neural network and updates the field class accordingly.
"""
def output_to_move(output, field, moves, tracker_x, tracker_y): # tracker is a list of moves made by the bot
    if max(output) == output[0]:
        field.push()

        moves.append("push") #update moves so we can see what is done
        # for plotting
        tracker_x.append(field.get_turt_x())
        tracker_y.append(field.get_turt_y())
    elif max(output) == output[1]:
        field.pivot_ccw()

        moves.append("pivot CCW") #update moves so we can see what is done
        # for plotting
        tracker_x.append(field.get_turt_x())
        tracker_y.append(field.get_turt_y())
    else:
        field.pivot_cw()

        moves.append("pivot CW") #update moves so we can see what is done
        # for plotting
        tracker_x.append(field.get_turt_x())
        tracker_y.append(field.get_turt_y())
    return field


"""
Evaluates genomes in a population.
Sets best_x and best_y if acceptable path is found.
"""
def evaluate(genomes, config):
    global best_x
    global best_y
    global flag_x
    global flag_y
    global turt_x
    global turt_y
    global turt_rad
    for genome_id, genome in genomes:
        net = neat.nn.recurrent.RecurrentNetwork.create(genome, config) # create networks from the genomes
        # f = randomField() # create a random field
        f = Field(turt_x, turt_y, turt_rad, flag_x, flag_y)
        print(f.distance_from_flag())

        #empty lists to track position
        tracker_x = [turt_x]
        tracker_y = [turt_y]
        moves = [] #track moves
        # initialize to furthest away it could be
        curr_distance = 10
        distance_min = 10
        # initialize to lowest fintess possible
        curr_fitness = 0 
        fitness_max = 0
        ineff_moves = 0 # count number of "inefficent" moves made before moving closer to flag (so we get an efficent network)
        done = False # will be done when either run out of time or get really close to flag
        while not done:
            # input values from the field into network
            nnOutput = net.activate([f.get_turt_x(), f.get_turt_y(), f.get_turt_rad(), f.get_flag_x(), f.get_flag_y()])
            f = output_to_move(nnOutput, f, moves, tracker_x, tracker_y) # move the turtlebot according to network

            if moves[-1] == "pivot CW" or moves[-1] == "pivot CCW": # negative reward for turning, disincentivizes "wiggly" paths
                curr_fitness += -1
            
            curr_distance = f.distance_from_flag()

            # if we made a move towards the final goal, then our fitness goes up by one
            if curr_distance < distance_min:
                # curr_fitness += abs(distance_min - curr_distance)
                curr_fitness += 1
                distance_min = curr_distance

            # if this is the max fintness we have had so far, set the inefficent moves to zero, otherwise incriment
            if curr_fitness > fitness_max:
                fitness_max = curr_fitness
                ineff_moves = 0
            else:
                ineff_moves += 1 # if inefficent moves gets to 7 (the number where turning the other way would be more efficent) and no progress has been made, genome fails
            
            # if we get within 1 unit from flag, 1000 reward and done (genome succeeds)
            if f.distance_from_flag() < (2/12.0): # 2 inches from flag = win
                done = True
                curr_fitness += 1000
                # for plotting
                best_x = tracker_x
                best_y = tracker_y
                print(genome_id, curr_fitness, f.distance_from_flag(), moves)
            # if too many inefficent moves, we are done and genome fails
            elif ineff_moves >= 10: # using 6 is the only time where the robot "knows" what a movement will do to it (i.e. here it knows how far it will turn each time so it can make efficent turns)
                done = True
                print(genome_id, curr_fitness, f.distance_from_flag())
            
            genome.fitness = curr_fitness

"""
Start of the actual program
"""

#configure the NEAT network
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config-feedforward')

p = neat.Population(config)

flag_x = 3
flag_y = 3
turt_x = 2
turt_y = 1
turt_rad = math.pi/2

best = p.run(evaluate) # would be nice to figure out how to pass things into genome, and get them out (avoid all the global variables)
# see the neural network
# visualize.draw_net(config, best, view=True)

# see the turtebot path
fig, ax = plt.subplots()
plt.xlim(0,4)
plt.ylim(0,4)
ax.set_aspect('equal') # make axis same scale
ax.plot(best_x, best_y, 'r--', turt_x, turt_y, 'bs', flag_x, flag_y, 'g^')  # plot path as red dashed line, goal as green line, 
plt.show() # without this it doesn't show up
