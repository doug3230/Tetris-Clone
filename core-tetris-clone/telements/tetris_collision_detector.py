'''
Created on Mar 6, 2016

@author: Richard
'''
from elements import GridRectCollisionDetector, ElementCollection, GridBoundaryElement
from tgame import grid_camera

class TetrisCollisionDetector(GridRectCollisionDetector, ElementCollection):
    def __init__(self):
        GridRectCollisionDetector.__init__(self, grid_rect=grid_camera(), grid_elements=[])
        ElementCollection.__init__(self, subelements=[])
        self.initialize_boundary()
        return
    
    def update(self):
        if self.subelements != self.grid_elements:
            self.refresh()
            self.subelements = self.grid_elements
        ElementCollection.update(self)
        return
    
    def add_element(self, element):
        GridRectCollisionDetector.insert_element(self, element)
        return
    
    def remove_element(self, element):
        GridRectCollisionDetector.remove_element(self, element)
        element.refresh()
        for dirty_rect in element.dirty_list:
            self.dirty_list.append(dirty_rect)
        element.dirty_list = []
        return
    
    def initialize_boundary(self):
        self.boundary = GridBoundaryElement(grid_camera=grid_camera())
        self.add_element(self.boundary)
        return
    
    def get_number_of_lines_to_clear(self):
        occupied_rows = []
        grid_rect = self.grid_rect
        for y in range(grid_rect.y, grid_rect.y + grid_rect.h):
            if self.is_row_all_occupied(y):
                occupied_rows.append(y)
        return len(occupied_rows)
    
    def clear_lines(self):
        occupied_rows = []
        grid_rect = self.grid_rect
        for y in range(grid_rect.y, grid_rect.y + grid_rect.h):
            if self.is_row_all_occupied(y):
                occupied_rows.append(y)
        for row in occupied_rows:
            for element in self.occupants_with_y(row):
                self.remove_element(element)
            for element in self.occupants_before_y(row):
                element.grid_position.y += 1
        if occupied_rows:
            self.recalculate_occupied_tiles()
        return