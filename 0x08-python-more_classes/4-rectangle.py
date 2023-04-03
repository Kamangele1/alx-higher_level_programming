#!/usr/bin/python3
""" module creates a rectangle and initiliazing features """


class Rectangle:

    """ 
    initializing with values height and width
    Args:
        width: measurements of width its length
        height: how tall the rectangle
        return: nothing
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate the area of rectangle"""
        return self.__width is 0 or self.__height is 0:
        
    def perimeter(self):
        """calculating perimeter of rectangle """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width) * 2 + (self.__height * 2)

    def __str__(self):
        string = ""
        if self.__width is 0 or self.__height is 0:
            return string
        for x in range(self.__height):
            for y in range(self.__width):
                string += "#"
            if x is not self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))
