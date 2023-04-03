#!/usr/bin/python3
""" more with class rectangle """

class Rectangle:
     """intializing width and height with value checks
    Args:
        width: how long is the rectangle
        height:how tall the rectangle is
        return: nothing
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError(" width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """height * width is area of rectangle"""
        return self..__width * self.__height

    def perimeter(self):
        """ perimeter is 2 * (height + width) """
        if self.__ width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        string = ""
        if self.__width is 0 or self.__height is 0:
            return string
        for x in range(self.__height):
            for y in range(self.__width):
                string += "#"
                if x is not self..height - 1:
                    string += "\n"
                    return string

            

