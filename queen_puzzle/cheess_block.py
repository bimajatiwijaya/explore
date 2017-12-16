# -*- coding: utf-8 -*-
import point

class ChessBlock(point.Point):
    """ Chess Block class """
    army = ''
    safe = True

    def __init__(self, army=None, safe=True):
        self.army = army
        self.safe = safe
    
    def set_block_status(self, safe=True):
        self.safe = safe
    
    def set_army(self, army=None):
        if army:
            self.army = army
    
    def get_block_status(self):
        return self.safe
