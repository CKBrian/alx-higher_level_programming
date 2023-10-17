#!/usr/bin/python3
""" module defines a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines a square that inherits from Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes the Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return square attributes as [Square] (<id>) <x>/<y> - <size>"""
        return "[{}] ({}) {}/{} - {}" \
            .format(self.__class__.__name__,
                    self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ value (int): size of the square sides """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns values to attributes"""
        i = 0
        for value in args:
            if not value:
                break
            if i == 0:
                self.id = value
            if i == 1:
                self.size = value
            if i == 2:
                self.x = value
            if i == 3:
                self.y = value
            i += 1
        for key, value in kwargs.items():
            if not kwargs:
                break
            if key == "id":
                self.id = value
            if key == "size":
                self.size = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    def to_dictionary(self):
        """ returns a dictionary representation of a square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
