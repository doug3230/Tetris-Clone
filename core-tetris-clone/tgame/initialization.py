'''
Created on Feb 28, 2016

@author: Richard
'''
class System:
    GRID_CAMERA = None

def grid_camera():
    return System.GRID_CAMERA

def initialize():
    initialize_grid_camera()
    return

def initialize_grid_camera():
    from elements import GridCamera
    from tcustomization.grid_settings import GRID_CAMERA_X, GRID_CAMERA_Y, \
    GRID_CAMERA_W, GRID_CAMERA_H, GRID_CAMERA_RECT
    System.GRID_CAMERA = GridCamera(x=GRID_CAMERA_X, y=GRID_CAMERA_Y,
                                    w=GRID_CAMERA_W, h=GRID_CAMERA_H,
                                    rect=GRID_CAMERA_RECT)
    return