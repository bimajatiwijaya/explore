# -*- coding: utf-8 -*-


class Point:
    """ class point """
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        """ constructor """
        self.x = x
        self.y = y
    
    def set_point(self, x=0, y=0):
        """ Set Point """
        self.x = x
        self.y = y

    def get_x(self):
        """ get x """
        return self.x

    def get_y(self):
        """ get y """
        return self.y
