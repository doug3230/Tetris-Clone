'''
Created on Mar 5, 2016

@author: Richard
'''
from constants import BLACK
from elements import ElementCollection, GridElement
from coloured_tile import init_ctile_at
from tcustomization import MAX_RANDOM_ROTATIONS
from random import randint

class Tetromino(GridElement):
    def __init__(self, colour=BLACK, grid_camera=None, tile_positions=tuple()):
        GridElement.__init__(self, element=ElementCollection(),
                             grid_position=TetrominoPosition(),
                             grid_camera=grid_camera)
        self.old_tile_positions = None
        self.tile_positions = tile_positions
        self.mapping = {}
        self.colour = colour
        self.reset_position_mapping()
        return
    
    def get_tiles(self):
        return self.element.subelements
    
    def rotate(self):
        self.tile_positions = tuple((position[1], -position[0]) \
                                    for position in self.tile_positions)
        min_x = min((position[0] for position in self.tile_positions))
        min_y = min((position[1] for position in self.tile_positions))
        self.tile_positions = tuple((-min_x + position[0], -min_y + position[1]) \
                                    for position in self.tile_positions)
        self.reset_position_mapping()
        return
    
    def rotate_randomly(self):
        rotations = randint(0, MAX_RANDOM_ROTATIONS)
        for i in range(rotations):
            self.rotate()
        return
    
    def reset_position_mapping(self):
        self.element.remove_all_elements()
        self.mapping = {}
        self.grid_position.tile_positions = self.tile_positions
        x = self.grid_position.x
        y = self.grid_position.y
        for position in self.tile_positions:
            tile = init_ctile_at(x=x + position[0],
                                y=y + position[1],
                                colour=self.colour,
                                grid_camera=self.grid_camera)
            self.mapping[position] = tile
            self.element.add_element(tile)
        return
    
    def update(self):
        self.element.rect = self.grid_camera.rect
        if self.tile_positions != self.grid_position.tile_positions:
            self.refresh()
            self.reset_position_mapping()
        for position in self.mapping.keys():
            tile = self.mapping[position]
            tile.colour = self.colour
            tile.grid_camera = self.grid_camera
            tile.grid_position.x = self.grid_position.x + position[0]
            tile.grid_position.y = self.grid_position.y + position[1]
        GridElement.update(self)
        return

from elements import GridPosition
class TetrominoPosition(GridPosition):
    def __init__(self, tile_positions=[], **kwargs):
        GridPosition.__init__(self, **kwargs)
        self.tile_positions = tile_positions
        return
    
    def occupied_tiles(self):
        return tuple((self.x + position[0], self.y + position[1]) \
                     for position in self.tile_positions)
    
    def rotation_positions(self):
        rot_positions = tuple((position[1], -position[0]) \
                              for position in self.tile_positions)
        min_x = min((position[0] for position in rot_positions))
        min_y = min((position[1] for position in rot_positions))
        rot_positions = tuple((-min_x + position[0], -min_y + position[1]) \
                              for position in rot_positions)
        return rot_positions
    
    def rotation_tiles(self):
        rot_positions = self.rotation_positions()
        return tuple((self.x + position[0], self.y + position[1]) \
                     for position in rot_positions)

def init_tetromino_at(classname=Tetromino, x=0, y=0, grid_camera=None):
    tetromino = classname(grid_camera=grid_camera)
    tetromino.grid_position.x = x
    tetromino.grid_position.y = y
    return tetromino
