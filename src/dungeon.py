"""
Created on Oct 2, 2015

@author: rmdobbins
"""
from src.cell import Cell


class Dungeon(object):
    """
    class docs
    """

    def set_perimeter_wall(self, grid):
        # top
        n = 0
        for _ in grid[0]:
            self.grid[0][n] = Cell.Border
            n += 1
        # left & right
        for row in grid:
            row[0] = Cell.Border
            row[-1] = Cell.Border

        # bottom
        n = 0
        for _ in grid[-1]:
            self.grid[-1][n] = Cell.Border
            n += 1

    def __init__(self, height, width):
        """
        Constructor
        """
        self.height = height
        self.width = width
        self.grid = [[Cell.Open for _ in range(height)] for _ in range(width)]
        self.set_perimeter_wall(self.grid)

    def print(self):
        for row in self.grid:
            for cell in row:
                if cell == Cell.Open :
                    print(chr(32), end='')
                if cell == Cell.Border :
                    print('\u2588', end='')
            print()
