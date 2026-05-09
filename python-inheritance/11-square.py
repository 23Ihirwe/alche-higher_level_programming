#!/usr/bin/python3
"""Module defining a Square with a custom print string."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that implements its own __str__."""

    def __init__(self, size):
        """Initializes size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
