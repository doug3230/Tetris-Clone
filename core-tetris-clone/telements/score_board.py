'''
Created on Mar 10, 2016

@author: Richard
'''
from copy import deepcopy
from elements import ElementCollection, Rectangle, Text, TextLines
from tcustomization import SCORE_BOARD_COLOUR, SCORE_BOARD_RECT, \
SCORE_TEXT_RECT, SCORE_TEXT_FONT_SIZE, NEXT_TEXT_RECT, NEXT_TEXT_FONT_SIZE, \
HOT_KEYS_TEXT_RECT, HOT_KEYS_TEXT_FONT_SIZE, HOT_KEYS_LINES_RECT, HOT_KEYS_LINES_FONT_SIZE, \
CONTROLS_TEXT_RECT, CONTROLS_TEXT_FONT_SIZE, CONTROLS_LINES_RECT, CONTROLS_LINES_FONT_SIZE, \
GAME_OVER_TEXT_RECT, GAME_OVER_TEXT_FONT_SIZE
from telements import NextTetrominoGridCamera

class ScoreBoard(ElementCollection):
    def __init__(self, score=0):
        self.background_rectangle = Rectangle(colour=SCORE_BOARD_COLOUR, rect=SCORE_BOARD_RECT, layer=-1)
        self.next_grid_camera = NextTetrominoGridCamera()
        self.score_text = Text(rect=SCORE_TEXT_RECT, font_size=SCORE_TEXT_FONT_SIZE)
        self.next_text = Text(rect=NEXT_TEXT_RECT, font_size=NEXT_TEXT_FONT_SIZE,
                              text="Next:")
        self.hot_keys_text = Text(rect=HOT_KEYS_TEXT_RECT, font_size=HOT_KEYS_TEXT_FONT_SIZE,
                                  text="Hot Keys:")
        self.hot_keys_text_lines = TextLines(rect=HOT_KEYS_LINES_RECT,
                                             font_size=HOT_KEYS_LINES_FONT_SIZE,
                                             text=["N - new game", "I - instructions",
                                                   "P - pause", "R - resume"])
        self.controls_text = Text(rect=CONTROLS_TEXT_RECT, font_size=CONTROLS_TEXT_FONT_SIZE,
                                  text="Controls:")
        self.controls_text_lines = TextLines(rect=CONTROLS_LINES_RECT,
                                             font_size=CONTROLS_LINES_FONT_SIZE,
                                             text=["Left - move", "Right - move",
                                                   "Down - drop", "Space - rotate"])
        self.game_over_text = TextLines(rect=GAME_OVER_TEXT_RECT,
                                        font_size=GAME_OVER_TEXT_FONT_SIZE,
                                        text=["Game", "Over"], bold=True)
        self.next_tetromino = None
        self.game_over = False
        subelements = [self.background_rectangle, self.score_text, self.next_text,
                       self.hot_keys_text, self.hot_keys_text_lines,
                       self.controls_text, self.controls_text_lines,
                       self.game_over_text]
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
        
        position.x = (camera.w - position.get_width()) // 2
        position.y = (camera.h - position.get_height()) // 2
        self.add_element(self.next_tetromino)
        return
    
    def add_lines_to_score(self, lines):
        score_for_lines = ((lines + 1) * lines) // 2
        self.score += score_for_lines
        return
    
    def update(self):
        self.score_text.text = "Score: {0:>3}".format(self.score)
        self.game_over_text.visible = self.game_over
        ElementCollection.update(self)
        return