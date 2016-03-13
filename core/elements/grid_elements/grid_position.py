'''
Created on Feb 28, 2016

@author: Richard
'''
class GridPosition:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        return
    
    def occupied_tiles(self):
        return ((self.x, self.y),)
    
    def occupied_tiles_relative(self, rel_x=0, rel_y=0):
        return ((tile[0] + rel_x, tile[1] + rel_y) for tile in self.occupied_tiles())