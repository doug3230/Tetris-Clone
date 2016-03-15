'''
Created on Mar 13, 2016

@author: Richard
'''
from elements import GridCamera
from tcustomization import GRID_CAMERA_W, GRID_CAMERA_H, GRID_CAMERA_RECT, \
NEXT_CAMERA_W, NEXT_CAMERA_H, NEXT_CAMERA_RECT

class TetrisGameGridCamera(GridCamera):
    def __init__(self):
        GridCamera.__init__(self, w=GRID_CAMERA_W, h=GRID_CAMERA_H,
                            rect=GRID_CAMERA_RECT)
        return

class NextTetrominoGridCamera(GridCamera):
    def __init__(self):
        GridCamera.__init__(self, w=NEXT_CAMERA_W, h=NEXT_CAMERA_H,
                            rect=NEXT_CAMERA_RECT)
        return