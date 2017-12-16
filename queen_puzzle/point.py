# -*- coding: utf-8 -*-


class Point:
    """ class point """
    x = 0
    y = 0

    def __init__(self):
        """ constructor """
        self.x = 0
        self.y = 0
    
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
    def get_coordinat(self):
        """ get x and y """
        return self.x, self.y
