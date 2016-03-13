'''
Created on Dec 6, 2015

@author: Richard
'''
from elements import Element

class DecorateElement(Element):
    def decorated_element(self):
        if not self.element:
            d_e = None
        else:
            d_e = self.element.decorated_element()
        return d_e
    
    def refresh(self):
        if self.element:
            self.element.refresh()
            for dirty_rect in self.element.dirty_list:
                self.dirty_list.append(dirty_rect)
            self.element.dirty_list = []
        return
    
    def update(self):
        if self.element:
            self.element.update()
            self.rect = self.element.rect
            for dirty_rect in self.element.dirty_list:
                self.dirty_list.append(dirty_rect)
            self.element.dirty_list = []
        Element.update(self)
        return