'''
Created on Mar 12, 2016

@author: Richard
'''
from elements import SubState, Rectangle
from telements import IntroStateText
from tcustomization import SCORE_BOARD_COLOUR, SCORE_BOARD_RECT

class IntroState(SubState):
    def __init__(self, parent=None):
        self.background_rectangle = Rectangle(colour=SCORE_BOARD_COLOUR, rect=SCORE_BOARD_RECT)
        self.intro_state_text = IntroStateText()
        subelements = [self.background_rectangle, self.intro_state_text]
        SubState.__init__(self, parent=parent, subelements=subelements)
        return