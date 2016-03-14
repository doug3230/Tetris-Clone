'''
Created on Mar 12, 2016

@author: Richard
'''
import pygame
from elements import StateSystem
from intro_state import IntroState
from game_state import GameState

class MainState(StateSystem):
    def __init__(self):
        StateSystem.__init__(self)
        self.intro_state = IntroState(parent=self)
        self.game_state = GameState(parent=self)
        self.show_instructions()
        return
    
    def handle_event(self, event):
        StateSystem.handle_event(self, event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                self.new_game()
            elif event.key == pygame.K_p:
                self.pause_game()
            elif event.key == pygame.K_r:
                self.resume_game()
            elif event.key == pygame.K_i:
                self.show_instructions()
        return
    
    def new_game(self):
        self.child_state = self.game_state
        self.game_state.new_game()
        self.refresh_screen = True
        return
    
    def resume_game(self):
        self.child_state = self.game_state
        self.game_state.unpause()
        self.refresh_screen = True
        return
    
    def pause_game(self):
        self.child_state = self.game_state
        self.game_state.pause()
        self.refresh_screen = True
        return
    
    def show_instructions(self):
        self.child_state = self.intro_state
        self.refresh_screen = True
        return