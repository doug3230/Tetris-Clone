'''
Created on Mar 12, 2016

@author: Richard
'''
from pygame import Rect
from elements import ElementCollection, Text, TextLines
from constants import BLACK
from telements import ScoreBoard

class IntroStateText(ElementCollection):
    def __init__(self):
        self.title_text = Text(text="Tetris Clone", bold=True,
                               font_size=35, font_colour=BLACK,
                               rect=Rect((20, 40), (360, 50)))
        self.instruction_heading_text = Text(text="Instructions:",
                               font_size=16, font_colour=BLACK,
                               bold=True, rect=Rect((20, 100), (360, 20)))
        instructions = ["Blocks will fall from the top.",
                        "Use the arrow keys to move the ",
                        "falling block left or right.",
                        "The down key can bring the block ",
                        "all the way down immediately.",
                        "The spacebar can be used to rotate",
                        "the falling block.",
                        "",
                        "Blocks are cleared when they fill",
                        "an entire horizontal line and ",
                        "points are scored based on ",
                        "the number of lines cleared ",
                        "at once.",
                        "",
                        "The game is over when blocks are ",
                        "piled all the way to the top and ",
                        "a new one cannot be dropped."]
        self.instruction_text = TextLines(text=instructions,
                               font_size=14, font_colour=BLACK,
                               rect=Rect((20, 120), (360, 410)))
        
        self.start_text = Text(text="Press the 'n' key to start", italic=True,
                               font_size=15, font_colour=BLACK, bold=True,
                               rect=Rect((20, 560), (360, 30)))
        subelements = [self.title_text, self.instruction_heading_text,
                       self.instruction_text, self.start_text]
        ElementCollection.__init__(self, subelements=subelements)
        return