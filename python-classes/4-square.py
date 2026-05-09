#!/usr/bin/python3
"""Module defining a Square with getters and setters."""


class Square:
    """Square class with property accessors."""

    def __init__(self, size=0):
        """Initialize the square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area."""
        return self.__size ** 2
