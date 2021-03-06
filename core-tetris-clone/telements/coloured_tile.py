'''
Created on Mar 5, 2016

@author: Richard
'''
from constants import BLACK
from tcustomization import COLOURED_TILE_MARGIN
from elements import GridTileElement, Rectangle, GridPosition, margin

class ColouredTile(GridTileElement):
    def __init__(self, colour=BLACK, grid_camera=None):
        element = Rectangle(colour=colour)
        element = margin(element, COLOURED_TILE_MARGIN)
        GridTileElement.__init__(self, element=element,
                                 grid_position=GridPosition(),
                                 grid_camera=grid_camera)
        self.colour = colour
        return
    
    def update(self):
        self.element.decorated_element().colour = self.colour 
        GridTileElement.update(self)
        return
    
def init_ctile_at(colour=BLACK, x=0, y=0, grid_camera=None):
    ctile = ColouredTile(colour=colour, grid_camera=grid_camera)
    ctile.grid_position.x = x
    ctile.grid_position.y = y
    return ctile