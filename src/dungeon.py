'''
Created on Oct 2, 2015

@author: rmdobbins
'''

class Dungeon(object):
    '''
    classdocs
    '''


    def wallPerimeter(self, grid):
        #top
        n=0
        for square in grid[0]:
            self.grid[0][n] = 1
            n += 1
        #left & right
        n=0
        for row in grid:
            row[0] = 1
            row[-1] = 1
            
        #bottom
        n=0
        for square in grid[-1]:
            self.grid[-1][n] = 1
            n += 1
        pass
    
    def __init__(self, height, width):
        '''
        Constructor
        '''
        self.height = height
        self.width = width
        self.grid = [[0 for x in range(height)] for x in range(width)] 
        self.wallPerimeter(self.grid)
        



