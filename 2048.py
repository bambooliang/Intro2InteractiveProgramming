"""
http://www.codeskulptor.org/#user46_Hxd9FkwJtX_27.py
（Codeskulptor is only compatible with Google Chrome.)
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    #move all non-zero digits to the left
    output = reallocate(line) 
    #merge same digits next to each other
    non_zero = 0
    while non_zero < len(output)-1:
        if output[non_zero] == output[non_zero+1]:
            output[non_zero] = output[non_zero] *2
            output[non_zero+1] = 0
            non_zero +=1
        non_zero+=1
        #move all non-zero digits to the left
    output = reallocate(output) 
    print(output)
    print
    return output

def reallocate(line):
    """
    This function move all 0 to the end of the array
    """
    output =[]
    
    for num in line:
        if num != 0:
            output.append(num) 
            
    if len(output) != len(line):
        for count in range (len(output),len(line)):
            output.append(0)
            output[count]=0
                      
    return output

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """ 
        Constructor. initiate values and create initial board
        """
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        
        #store the initial value of the array for direction
        self.direction_array = {}
        self.direction_array[UP] = [[0,dummy_col] for dummy_col in range (0,grid_width)]
        self.direction_array[DOWN] = [[grid_height-1,dummy_col] for dummy_col in range (0,grid_width)]
        self.direction_array[LEFT] = [[dummy_row,0] for dummy_row in range (0,grid_height)]
        self.direction_array[RIGHT] = [[dummy_row,grid_width-1] for dummy_row in range (0,grid_height)]
  
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_col in range(self.grid_width)]
                           for dummy_row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        print out grid
        """
        print "Print out values in grid"
        game_grid = ""
        
        for dummy_row in self.grid:
            game_grid += str(dummy_row)
            game_grid += "\n"
        
        return game_grid


    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        #initiate value
        tile_moved = False
        num_step = 0
        row = 0
        col = 0 
        
        #define # in that array
        if direction < 3:
            num_step = self.grid_height
        else:
            num_step = self.grid_width
            
        #loop through each row 
        for dummy_position in self.direction_array[direction]:
            merge_array = []
            temp_array = []
            row = dummy_position[0]
            col = dummy_position[1]
            for dummy_step in range(num_step):
                merge_array.append(self.get_tile(row,col))
                temp_array.append(self.get_tile(row,col))
                row += OFFSETS[direction][0]
                col +=  OFFSETS[direction][1]
                
            merge_array = merge (merge_array)
            
            if merge_array != temp_array:
                tile_moved = True
                
                row = dummy_position[0]
                col = dummy_position[1]
                for dummy_step in range(num_step):
                    self.set_tile(row, col, merge_array[dummy_step])
                    row += OFFSETS[direction][0]
                    col +=  OFFSETS[direction][1]
                    
        if tile_moved == True:
            self.new_tile()
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #select row and column until it is empty
        pop_row = random.randrange(0,self.grid_height)
        pop_col = random.randrange(0,self.grid_width)
        while self.grid[pop_row][pop_col] != 0:
            pop_row = random.randrange(0,self.grid_height)
            pop_col = random.randrange(0,self.grid_width)
        #post value when it is empty
        if random.random() <=0.1:
            self.grid[pop_row][pop_col] = 4
        else:
            self.grid[pop_row][pop_col] = 2

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
