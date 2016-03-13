'''
Created on Mar 6, 2016

@author: Richard
'''
from grid_collision_detector import GridCollisionDetector

class GridRectCollisionDetector(GridCollisionDetector):
    def __init__(self, grid_rect=None, **kwargs):
        GridCollisionDetector.__init__(self, **kwargs)
        self.grid_rect = grid_rect
        return
    
    def occupants_with_x(self, x):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(x, grid_rect.y, 1, grid_rect.h)
    
    def occupants_with_y(self, y):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(grid_rect.x, y, grid_rect.w, 1)
    
    def occupants_before_x(self, x):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(grid_rect.x, grid_rect.y, x - grid_rect.x, grid_rect.h)
    
    def occupants_after_x(self, x):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(x + 1, grid_rect.y,
                                      grid_rect.w - (x + 1), grid_rect.h)
        
    def occupants_before_y(self, y):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(grid_rect.x, grid_rect.y, grid_rect.w, y - grid_rect.y)
    
    def occupants_after_y(self, y):
        grid_rect = self.grid_rect
        return self.occupants_in_rect(grid_rect.x, y + 1,
                                      grid_rect.w, grid_rect.h - (y + 1))
        
    def is_row_all_occupied(self, y):
        occupied = True
        grid_rect = self.grid_rect
        for x in range(grid_rect.x, grid_rect.x + grid_rect.w):
            if not self.is_tile_occupied(x, y):
                occupied = False
                break
        return occupied
    
    def is_col_all_occupied(self, x):
        occupied = True
        grid_rect = self.grid_rect
        for y in range(grid_rect.y, grid_rect.y + grid_rect.h):
            if not self.is_tile_occupied(x, y):
                occupied = False
                break
        return occupied