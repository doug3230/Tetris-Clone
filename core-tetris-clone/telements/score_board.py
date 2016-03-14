'''
Created on Mar 10, 2016

@author: Richard
'''
from copy import deepcopy
from pygame import Rect
from elements import ElementCollection, Rectangle, Text
from tcustomization import SCORE_BOARD_COLOUR, SCORE_BOARD_RECT
from telements import NextTetrominoGridCamera

class ScoreBoard(ElementCollection):
    def __init__(self, score=0):
        self.background_rectangle = Rectangle(colour=SCORE_BOARD_COLOUR, rect=SCORE_BOARD_RECT, layer=-1)
        self.next_grid_camera = NextTetrominoGridCamera()
        self.score_text = Text(rect=Rect((305, 10), (100, 17)), font_size=15)
        self.next_text = Text(rect=Rect((305, 30), (100, 17)), font_size=15)
        self.next_tetromino = None
        subelements = [self.background_rectangle, self.next_text, self.score_text]
        ElementCollection.__init__(self, subelements=subelements)
        self.score = score
        return
    
    def set_next_tetromino(self, tetromino):
        if self.next_tetromino is not None:
            self.remove_element(self.next_tetromino)
        self.next_tetromino = deepcopy(tetromino)
        
        camera = self.next_grid_camera
        self.next_tetromino.grid_camera = camera
        position = self.next_tetromino.grid_position
        
        position.x = camera.x + (camera.w - position.get_width()) // 2
        position.y = 0
        self.add_element(self.next_tetromino)
        return
    
    def add_lines_to_score(self, lines):
        score_for_lines = ((lines + 1) * lines) // 2
        self.score += score_for_lines
        return
    
    def update(self):
        self.next_text.text = "Next:"
        self.score_text.text = "Score: {0:>3}".format(self.score)
        ElementCollection.update(self)
        return