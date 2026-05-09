#!/usr/bin/python3
"""Module defining a Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class using BaseGeometry validation."""

    def __init__(self, width, height):
        """Initialize rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
