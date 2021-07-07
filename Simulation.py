import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Environment import Environment
from Agent import Agent
from Constants import Codes
from AgentType import Red, Blue
import Utils

GRID_SIZE = 70
INITIAL_FOOD = 10
FOOD_TIME = 1


type_red = Red()
type_blue = Blue()
codes = Codes()
colours = [[255,255,255],[255,0,0],[0,0,255],[0,0,0]]
reds = type_red.initial_population
blues = type_blue.initial_population
red_locations, blue_locations, food_locations = Utils.initialize_locations(reds,blues,GRID_SIZE,INITIAL_FOOD)
red = Agent(red_locations,type_red)
blue = Agent(blue_locations,type_blue)
env = Environment(GRID_SIZE,red_locations,blue_locations,food_locations)

fig = plt.figure()

def create_grid():
    grid = [[colours[0] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = colours[env.grid[i][j]]
    return grid

im = plt.imshow(create_grid(), animated = True)

time = 1

def update_grid(*args):
    global time
    if(time%FOOD_TIME==0):
        Utils.add_food(food_locations,blue,red,env)
    Utils.remove(blue,env)
    Utils.remove(red,env)
    if(red.population == 0 or blue.population == 0):
        ani.event_source.stop()
    if(time%2==0):
        Utils.update_locations(red, env)
        Utils.update_locations(blue, env)
    else:
        Utils.update_locations(blue, env)
        Utils.update_locations(red, env)
    Utils.split(blue,food_locations,env)
    Utils.split(red,food_locations,env)
    blue.decrease_health()
    red.decrease_health()
    time = time + 1
    im.set_array(create_grid())
    return im,

ani = animation.FuncAnimation(fig,update_grid,interval=40,blit = True)

plt.show()


