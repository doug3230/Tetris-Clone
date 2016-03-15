'''
Created on Mar 7, 2016

@author: Richard
'''
from random import choice
import pygame, game
from elements import SubState
from telements import ScoreBoard, TetrisCollisionDetector, \
TetrisGameGridCamera, init_tetromino_at, PIECES
from tcustomization import GAME_FALL_SECONDS

class GameState(SubState):
    def __init__(self, parent=None, fall_seconds=GAME_FALL_SECONDS):
        SubState.__init__(self, parent=parent, subelements=[])
        self.fall_seconds = fall_seconds
        self.new_game()
        return
    
    def new_game(self):
        self.remove_all_elements()
        self.grid_camera = TetrisGameGridCamera()
        self.collision_detector = TetrisCollisionDetector(grid_camera=self.grid_camera)
        self.score_board = ScoreBoard()
        self.add_element(self.collision_detector)
        self.add_element(self.score_board)
        self.next_piece = self.generate_piece()
        self.add_next_piece()
        self.reset_next_fall_time()
        self.paused = False
        self.game_over = False
        return
    
    def pause(self):
        self.paused = True
        return
    
    def unpause(self):
        self.paused = False
        return
    
    def reset_next_fall_time(self):
        self.next_fall_time = game.current_time_in_ms() + self.fall_seconds*1000
        return
    
    def is_past_next_fall_time(self):
        return game.current_time_in_ms() > self.next_fall_time
    
    def generate_piece(self):
        classname = choice(PIECES)
        top_middle = self.grid_camera.top_middle()
        x = top_middle[0]
        y = top_middle[1]
        instance = init_tetromino_at(classname=classname, x=x, y=y,
                                     grid_camera=self.grid_camera)
        instance.rotate_randomly()
        return instance
    
    def add_next_piece(self):
        self.current_piece = self.next_piece
        self.next_piece = self.generate_piece()
        self.add_element(self.current_piece)
        self.current_piece.update()
        self.game_over = not self.can_move_current_piece(0, 1)
        self.score_board.set_next_tetromino(self.next_piece)
        self.reset_next_fall_time()
        return
    
    def move_current_piece(self, x, y):
        position = self.current_piece.grid_position
        if self.can_move_current_piece(x, y):
            position.x += x
            position.y += y
        return
    
    def descend_current_piece(self):
        position = self.current_piece.grid_position
        can_descend = True
        while can_descend:
            old_y = position.y
            self.move_current_piece(0, 1)
            new_y = position.y
            can_descend = (old_y != new_y)
        self.convert_piece_to_tiles()
        self.add_next_piece()
        self.reset_next_fall_time()
        return
    
    def rotate(self):
        can_rotate = True
        for tile in self.current_piece.grid_position.rotation_tiles():
            if self.collision_detector.is_tile_occupied(tile[0], tile[1]):
                can_rotate = False
                break
        if can_rotate:
            self.current_piece.rotate()
        return
    
    def convert_piece_to_tiles(self):
        cd = self.collision_detector
        self.current_piece.update()
        self.remove_element(self.current_piece)
        for element in self.current_piece.get_tiles():
            cd.insert_element(element)
        number_of_lines_to_clear = cd.get_number_of_lines_to_clear()
        self.score_board.add_lines_to_score(number_of_lines_to_clear)
        cd.clear_lines()
        return
    
    def can_move_current_piece(self, x, y):
        position = self.current_piece.grid_position
        can_move = True
        for tile in position.occupied_tiles_relative(rel_x=x,rel_y=y):
            if self.collision_detector.is_tile_occupied(tile[0], tile[1]):
                can_move = False
                break
        return can_move
    
    def handle_event(self, event):
        SubState.handle_event(self, event)
        if event.type == pygame.KEYDOWN and not self.paused:
            if event.key == pygame.K_SPACE:
                self.rotate()
            elif event.key == pygame.K_LEFT:
                self.move_current_piece(-1, 0)
            elif event.key == pygame.K_RIGHT:
                self.move_current_piece(1, 0)
            elif event.key == pygame.K_DOWN:
                self.descend_current_piece()
        return
    
    def update(self):
        if self.game_over or self.paused:
            pass
        elif self.is_past_next_fall_time():
            old_y = self.current_piece.grid_position.y
            self.move_current_piece(0, 1)
            new_y = self.current_piece.grid_position.y
            if old_y == new_y:
                self.convert_piece_to_tiles()
                self.add_next_piece()
            self.reset_next_fall_time()
        self.score_board.game_over = self.game_over
        SubState.update(self)
        return