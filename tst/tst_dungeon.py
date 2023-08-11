'''
Created on Oct 2, 2015

@author: rmdobbins
'''
import unittest
import src.dungeon


class Test(unittest.TestCase):


    def test_Generate100x100(self):
        d = src.dungeon.Dungeon(100,100)
        self.assertEqual(d.width, 100, 'Width not right.')
        self.assertEqual(d.height, 100, 'Height not right.')
        self.assertEqual(len(d.grid), 100, 'Grid height does not match.')
        self.assertEqual(len(d.grid[0]), 100, 'Grid width does not match.')
        
    def test_Generate10x10(self):
        d = src.dungeon.Dungeon(10,10)
        self.assertEqual(d.width, 10, 'Width not right.')
        self.assertEqual(d.height, 10, 'Height not right.')
        self.assertEqual(len(d.grid), 10, 'Grid height does not match.')
        self.assertEqual(len(d.grid[0]), 10, 'Grid width does not match.')

    def test_DungeonHasOuterWall(self):
        d = src.dungeon.Dungeon(3,3)
        self.assertEqual(d.grid[0][0], src.dungeon.Cell.Border, 'should be a border')
        self.assertEqual(d.grid[0][1], src.dungeon.Cell.Border, 'should be a border')
        self.assertEqual(d.grid[0][2], src.dungeon.Cell.Border, 'should be a border')
        self.assertEqual(d.grid[1][0], src.dungeon.Cell.Border, 'should be a border')
        self.assertEqual(d.grid[1][1], src.dungeon.Cell.Open, 'should be floor')
        self.assertEqual(d.grid[1][2], src.dungeon.Cell.Border, 'should be a border')
        self.assertEqual(d.grid[2][0], src.dungeon.Cell.Border, 'should be a border')
        self.assertEqual(d.grid[2][1], src.dungeon.Cell.Border, 'should be a border')
        self.assertEqual(d.grid[2][2], src.dungeon.Cell.Border, 'should be a border')
    
    def test_DungeonHasOuterWallbigger(self):
        d = src.dungeon.Dungeon(5,5)
        self.assertEqual(d.grid[0][0], src.dungeon.Cell.Border, 'should be a border')
        self.assertEqual(d.grid[1][1], src.dungeon.Cell.Open, 'should be a floor')
        self.assertEqual(d.grid[2][2], src.dungeon.Cell.Open, 'should be floor')
        self.assertEqual(d.grid[3][3], src.dungeon.Cell.Open, 'should be a floor')
        self.assertEqual(d.grid[4][4], src.dungeon.Cell.Border, 'should be a border')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_Generate100x100']
    unittest.main()