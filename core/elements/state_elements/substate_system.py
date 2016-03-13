'''
Created on Dec 13, 2015

@author: Richard
'''
from state_system import StateSystem
from substate import SubState

class SubStateSystem(StateSystem, SubState):
    def __init__(self, child_state=None, parent=None, **kwargs):
        SubState.__init__(self, parent=None)
        StateSystem.__init__(self, child_state=child_state, **kwargs)
        return