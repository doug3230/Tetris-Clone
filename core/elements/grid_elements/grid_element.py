'''
Created on Feb 28, 2016

@author: Richard
'''
from elements import Element, DecorateElement

class GridElement(DecorateElement):
    def __init__(self, element=None, grid_position=None, \
                 grid_camera=None, **kwargs):
        Element.__init__(self, **kwargs)
        self.element = element
        if element:
            self.rect = element.rect
        self.grid_position = grid_position
        self.grid_camera = grid_camera
        return
    
    def draw(self, screen):
        if self.element is not None and \
        (self.grid_camera is None or \
         self.grid_camera.rect.contains(self.element.rect)):
            self.element.draw(screen)
        return