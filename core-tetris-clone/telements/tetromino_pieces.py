'''
Created on Mar 9, 2016

@author: Richard
'''
from tetromino import Tetromino
from tcustomization import \
IPIECE_COLOUR, JPIECE_COLOUR, LPIECE_COLOUR, OPIECE_COLOUR, \
SPIECE_COLOUR, TPIECE_COLOUR, ZPIECE_COLOUR

class IPiece(Tetromino):
    def __init__(self, grid_camera=None):
        Tetromino.__init__(self, colour=IPIECE_COLOUR,
                           tile_positions=[(0, 0), (1, 0), (2, 0), (3, 0)],
                           grid_camera=grid_camera)
        return

class JPiece(Tetromino):
    def __init__(self, grid_camera=None):
        Tetromino.__init__(self, colour=JPIECE_COLOUR,
                           tile_positions=[(1, 0), (1, 1), (1, 2), (0, 2)],
                           grid_camera=grid_camera)
        return

class LPiece(Tetromino):
    def __init__(self, grid_camera=None):
        Tetromino.__init__(self, colour=LPIECE_COLOUR,
                           tile_positions=[(0, 0), (0, 1), (0, 2), (1, 2)],
                           grid_camera=grid_camera)
        return

class OPiece(Tetromino):
    def __init__(self, grid_camera=None):
        Tetromino.__init__(self, colour=OPIECE_COLOUR,
                           tile_positions=[(0, 0), (1, 0), (0, 1), (1, 1)],
                           grid_camera=grid_camera)
        return

class SPiece(Tetromino):
    def __init__(self, grid_camera=None):
        Tetromino.__init__(self, colour=SPIECE_COLOUR,
                           tile_positions=[(1, 0), (2, 0), (0, 1), (1, 1)],
                           grid_camera=grid_camera)
        return

class TPiece(Tetromino):
    def __init__(self, grid_camera=None):
        Tetromino.__init__(self, colour=TPIECE_COLOUR,
                           tile_positions=[(0, 0), (1, 0), (2, 0), (1, 1)],
                           grid_camera=grid_camera)
        return

class ZPiece(Tetromino):
    def __init__(self, grid_camera=None):
        Tetromino.__init__(self, colour=ZPIECE_COLOUR,
                           tile_positions=[(0, 0), (1, 0), (1, 1), (2, 1)],
                           grid_camera=grid_camera)
        return
