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

#configure the NEAT network
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config-feedforward')

# create a Field with random values; flag at least two units away from start
def randomField():
    # assume flag is too close until we find otherwise
    atLeast2away = False
    while not atLeast2away:
        turtx = random.randrange(0, constants.FIELD_X_MAX)
        turty = random.randrange(0, constants.FIELD_Y_MAX)
        rad = random.randrange(0, 628)/100.0 # about between 0 and 2*pi
        flagx = random.randrange(0, constants.FIELD_X_MAX)
        flagy = random.randrange(0, constants.FIELD_Y_MAX)
        
        f = Field(turtx, turty, rad, flagx, flagy)

        # if flag is far enough away, then we are done
        if f.distanceFromFlag() > 2:
            atLeast2away = True
    return(f)

# take an output from the neural network and have it move
def output_to_move(output, field, moves, trackerx, trackery): # tracker is a list of moves made by the bot
    if max(output) == output[0]:
        field.push()

        moves.append("push") #update moves so we can see what is done
        # for plotting
        trackerx.append(field.getTurtx())
        trackery.append(field.getTurty())
    elif max(output) == output[1]:
        field.pivotCCW()

        moves.append("pivot CCW") #update moves so we can see what is done
        # for plotting
        trackerx.append(field.getTurtx())
        trackery.append(field.getTurty())


    else:
        field.pivotCW()

        moves.append("pivot CW") #update moves so we can see what is done
        # for plotting
        trackerx.append(field.getTurtx())
        trackery.append(field.getTurty())
    return field

def evaluate(genomes, config):
    global bestx
    global besty
    global flagx
    global flagy
    global turtx
    global turty
    global turtrad
    for genome_id, genome in genomes:
        net = neat.nn.recurrent.RecurrentNetwork.create(genome, config) # create networks from the genomes
        # f = randomField() # create a random field
        f = Field(turtx, turty, turtrad, flagx, flagy)
        print(f.distanceFromFlag())

        #empty lists to track position
        trackerx = [turtx]
        trackery = [turty]
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
            nnOutput = net.activate([f.getTurtx(), f.getTurty(), f.getTurtrad(), f.getFlagx(), f.getFlagy()])
            f = output_to_move(nnOutput, f, moves, trackerx, trackery) # move the turtlebot according to network

            if moves[-1] == "pivot CW" or moves[-1] == "pivot CCW": # negative reward for turning, disincentivizes "wiggly" paths
                curr_fitness += -1
            
            curr_distance = f.distanceFromFlag()

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
            if f.distanceFromFlag() < (2/12.0): # 2 inches from flag = win
                done = True
                curr_fitness += 1000
                # for plotting
                bestx = trackerx
                besty = trackery
                print(genome_id, curr_fitness, f.distanceFromFlag(), moves)
            # if too many inefficent moves, we are done and genome fails
            elif ineff_moves >= 6: # using 6 is the only time where the robot "knows" what a movement will do to it (i.e. here it knows how far it will turn each time so it can make efficent turns)
                done = True
                print(genome_id, curr_fitness, f.distanceFromFlag())
            
            genome.fitness = curr_fitness


#configure the NEAT network
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config-feedforward')

p = neat.Population(config)

global bestx
global besty
global flagx
global flagy
global turtx
global turty

flagx = 3
flagy = 2
turtx = 1
turty = 1
turtrad = math.pi/2

best = p.run(evaluate) # would be nice to figure out how to pass things into genome, and get them out (avoid all the global variables)
# see the neural network
# visualize.draw_net(config, best, view=True)

# see the turtebot path
fig, ax = plt.subplots()
plt.xlim(0,4)
plt.ylim(0,4)
ax.set_aspect('equal') # make axis same scale
ax.plot(bestx, besty, 'r--', turtx, turty, 'bs', flagx, flagy, 'g^')  # plot path as red dashed line, goal as green line, 
plt.show() # without this it doesn't show up
