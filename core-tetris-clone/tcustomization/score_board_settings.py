'''
Created on Mar 3, 2016

@author: Richard
'''
from constants import WHITE
SCORE_BOARD_COLOUR = WHITE
from pygame import Rect
from customization import INIT_SCREEN_SIZE
from grid_settings import GRID_CAMERA_RECT
SCORE_BOARD_H_DIST = 1
SCORE_BOARD_RECT = Rect((GRID_CAMERA_RECT.right + SCORE_BOARD_H_DIST, GRID_CAMERA_RECT.top),
                        (INIT_SCREEN_SIZE[0] - GRID_CAMERA_RECT.right - SCORE_BOARD_H_DIST
                         , INIT_SCREEN_SIZE[1]))