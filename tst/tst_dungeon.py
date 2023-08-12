'''
Created on Oct 2, 2015

@author: rmdobbins
'''
import unittest
from src.dungeon import Dungeon
from src.cell import Cell


class Test(unittest.TestCase):


    def test_Generate100x100(self):
        d = Dungeon(100,100)
        self.assertEqual(d.width, 100, 'Width not right.')
        self.assertEqual(d.height, 100, 'Height not right.')
        self.assertEqual(len(d.grid), 100, 'Grid height does not match.')
        self.assertEqual(len(d.grid[0]), 100, 'Grid width does not match.')
        
    def test_Generate10x10(self):
        d = Dungeon(10,10)
        self.assertEqual(d.width, 10, 'Width not right.')
        self.assertEqual(d.height, 10, 'Height not right.')
        self.assertEqual(len(d.grid), 10, 'Grid height does not match.')
        self.assertEqual(len(d.grid[0]), 10, 'Grid width does not match.')

    def test_DungeonHasOuterWall(self):
        d = Dungeon(3,3)
        self.assertEqual(d.grid[0][1], Cell.Border, 'should be a border')
        self.assertEqual(d.grid[0][2], Cell.Border, 'should be a border')
        self.assertEqual(d.grid[0][0], Cell.Border, 'should be a border')
        self.assertEqual(d.grid[1][0], Cell.Border, 'should be a border')
        self.assertEqual(d.grid[1][1], Cell.Open, 'should be floor')
        self.assertEqual(d.grid[1][2], Cell.Border, 'should be a border')
        self.assertEqual(d.grid[2][0], Cell.Border, 'should be a border')
        self.assertEqual(d.grid[2][1], Cell.Border, 'should be a border')
        self.assertEqual(d.grid[2][2], Cell.Border, 'should be a border')
    
    def test_DungeonHasOuterWallbigger(self):
        d = Dungeon(5,5)
        self.assertEqual(d.grid[0][0], Cell.Border, 'should be a border')
        self.assertEqual(d.grid[1][1], Cell.Open, 'should be a floor')
        self.assertEqual(d.grid[2][2], Cell.Open, 'should be floor')
        self.assertEqual(d.grid[3][3], Cell.Open, 'should be a floor')
        self.assertEqual(d.grid[4][4], Cell.Border, 'should be a border')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_Generate100x100']
    unittest.main()