# -*- coding: utf-8 -*-
import point

class ChessBlock(point.Point):
    """ Chess Block class """
    army = ''
    safe = True

    def __init__(self):
        self.army = ''
        self.safe = True

    def set_block_status(self, safe=True):
        self.safe = safe

    def set_chess_block(self, x=0, y=0, army=""):
        self.x = x
        self.y = y
        self.army = army

    def is_safe(self):
        """ is position safe """
        return self.safe

    def set_army(self, army=None):
        """ Assign army """
        if army:
            self.army = army
            self.safe = False

    def get_status(self):
        """ Get block status """
        return self.safe

    def get_army(self):
        """ Get army """
        return self.army

    def set_not_safe(self):
        """ Set status """
        self.safe = False

    def attack_queen_block(self):
        """ Set status """
        if self.army == 'queen':
            self.safe = False
            return True
        else:
            self.safe = False
            return False
