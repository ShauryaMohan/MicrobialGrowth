from Constants import Codes
codes = Codes()
class Environment:
    def __init__(self,size,red,blue,foods):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        locations_list = [red, blue,foods]
        idx = 1
        for locations in locations_list:
            for location in locations:
                row, col = self.convert(location)
                self.grid[row][col] = idx
            idx = idx + 1

    def convert(self,location):
        return location//self.size, location%self.size

    def change_location(self,initial_location,new_location):
        row, col = self.convert(initial_location)
        nrow, ncol = self.convert(new_location)
        self.grid[nrow][ncol] = self.grid[row][col]
        self.grid[row][col] = codes.empty

    def add(self,location,code):
        row, col = self.convert(location)
        self.grid[row][col] = code
    
    def remove(self,location):
        row, col = self.convert(location)
        self.grid[row][col] = codes.empty

    def is_empty(self,location):
        row, col = self.convert(location)
        return (self.grid[row][col] == codes.empty or self.grid[row][col] == codes.food)
    
    def get_state(self):
        return self.grid