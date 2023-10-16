#!/usr/bin/python3
"""a module which defines a Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
        defines a Rectangle that inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Attributes:
            __width (int): Rectangle width
            __height (int): Rectangle height
            __x (): object x
            __y ():  object y
            id (int): id

        self.__height = height
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ value (int): Width value """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        else:
            self.__width = value

    @property
    def height(self):
        """ value (int): height value """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        else:
            self.__height = value

    @property
    def x(self):
        """ value (int): x value """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        else:
            self.__x = value

    @property
    def y(self):
        """ value (int): y value """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        else:
            self.__y = value

    def area(self):
        """ Return Rectangle area"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print(self.__y * "\n" +
              ("\n".join((self.__x * " ") + "#" *
               self.__width for _ in range(self.__height))))

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{}] ({}) {}/{} - {}/{}" \
            .format(self.__class__.__name__, self.id, self.__x, self.__y,
                    self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        i = 0
        for value in args:
            if not value:
                break
            if i == 0:
                self.id = value
            if i == 1:
                self.width = value
            if i == 2:
                self.height = value
            if i == 3:
                self.x = value
            if i == 4:
                self.y = value
            i += 1
        for key, value in kwargs.items():
            if not kwargs:
                break
            if key == "id":
                self.id = value
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle
            {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}"""
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
