'''
Created on Mar 10, 2016

@author: Richard
'''
from pygame import Rect
from elements import ElementCollection, Rectangle, Text
from tcustomization import SCORE_BOARD_COLOUR, SCORE_BOARD_RECT

class ScoreBoard(ElementCollection):
    def __init__(self, score=0):
        self.background_rectangle = Rectangle(colour=SCORE_BOARD_COLOUR, rect=SCORE_BOARD_RECT)
        self.score_text = Text(rect=Rect((305, 10), (100, 40)), font_size=15)
        subelements = [self.background_rectangle, self.score_text]
        ElementCollection.__init__(self, subelements=subelements)
        self.score = score
        return
    
    def add_lines_to_score(self, lines):
        score_for_lines = ((lines + 1) * lines) // 2
        self.score += score_for_lines
        return
    
    def update(self):
        self.score_text.text = "Score: {0:>3}".format(self.score)
        ElementCollection.update(self)
        return