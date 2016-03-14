'''
Created on Mar 13, 2016

@author: Richard
'''
from elements import GridCamera
from tcustomization.grid_settings import GRID_CAMERA_X, GRID_CAMERA_Y, \
GRID_CAMERA_W, GRID_CAMERA_H, GRID_CAMERA_RECT

class TetrisGameGridCamera(GridCamera):
    def __init__(self):
        GridCamera.__init__(self, x=GRID_CAMERA_X, y=GRID_CAMERA_Y,
                            w=GRID_CAMERA_W, h=GRID_CAMERA_H,
                            rect=GRID_CAMERA_RECT)
        return

class NextTetrominoGridCamera(GridCamera):
    def __init__(self):
        from pygame import Rect
        GridCamera.__init__(self, x=0, y=0, w=4, h=4,
                            rect=Rect((304, 48), (92, 92)))
        return