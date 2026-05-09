#!/usr/bin/python3
"""Module that compares rectangle areas."""


class Rectangle:
    """Class that defines a rectangle with static compare method."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """String representation."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                          for i in range(self.__height)])

    def __repr__(self):
        """Eval representation."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletion message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
