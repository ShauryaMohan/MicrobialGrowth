from Constants import Codes
import numpy as np

code = Codes()

def initialize_locations(reds,blues,n,food):
    locations = list(range(n*n))
    np.random.shuffle(locations)
    red_locations = locations[0:reds]
    blue_locations = locations[reds:reds+blues]
    food_locations = locations[reds+blues:reds+blues+food]
    return red_locations, blue_locations, food_locations

def get_neighbours(row,col):
    return [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]

def is_legal(cell,size):
    row, col = cell
    return (row >= 0 and row < size and col >= 0 and col < size)

def find_food(location,env):
    queue = []
    queue.append(location)
    visited = [[False for _ in range(env.size)] for _ in range(env.size)]
    while(len(queue) != 0):
        loc = queue.pop(0)
        r,c = env.convert(loc)
        if (env.grid[r][c] == code.food):
            return r,c
        neighbours = get_neighbours(r,c)
        for neighbour in neighbours:
            i,j = neighbour
            if is_legal(neighbour,env.size) and not visited[i][j]:
                queue.append(env.size*i + j)
                visited[i][j] = True
    return -1,-1

def get_direction(location,env,vision):
    frow,fcol = find_food(location,env)
    if (frow == -1 and fcol == -1):
        return location
    row, col = env.convert(location)
    if(abs(frow-row) > abs(fcol-col)):
        if frow - row > 0:
            return (row + 1)*env.size + col
        else:
            return (row - 1)*env.size + col
    else:
        if fcol - col > 0:
            return row*env.size + col + 1
        else:
            return row*env.size + col - 1
    
            
    
def update_locations(virus, env):
    for idx in range(len(virus.locations)):
        newLocation = get_direction(virus.locations[idx],env,virus.vision)
        if(newLocation == -1):
            continue
        if (env.is_empty(newLocation)):
            env.change_location(virus.locations[idx],newLocation)
            virus.update_location(idx,newLocation)
    if not virus.sanity():
        raise Exception('Please check the sanity of Agent has been breached!')

def remove(virus,env):
    locations = virus.remove()
    for location in locations:
        env.remove(location)
    if not virus.sanity():
        raise Exception('Please check the sanity of Agent has been breached!')

def split(virus,foods,env):
    to_remove = []
    idx = 0
    for location in virus.locations:
        if location in foods:
            to_remove.append(location)
            virus.increase_health(idx)
        idx = idx + 1
    for element in to_remove:
        foods.remove(element)
        env.remove(element)
        env.add(element,virus.code)
        row,col = env.convert(element)
        neighbours = get_neighbours(row,col)
        np.random.shuffle(neighbours)
        for neighbour in neighbours:
            r,c = neighbour
            if is_legal(neighbour,env.size) and env.is_empty(env.size*r + c):
                virus.add(env.size*r + c,virus.default_health)
                env.add(env.size*r + c, virus.code)
                break
    if not virus.sanity():
        raise Exception('Please check the sanity of Agent has been breached!')

def add_food(food_locations,blue,red,env):
    locations = food_locations + blue.locations + red.locations
    food = 1
    while(food != 0):
        n = np.random.randint(0,env.size*env.size)
        if n not in locations:
            food_locations.append(n)
            env.add(n,code.food)
            food = food - 1
    
    