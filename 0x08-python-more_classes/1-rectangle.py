#!/usr/bin/python3
"""This is a brief documentation of my module
It provides a brief overview of the module's purpose and functionality.
"""


class Rectangle:
    """A class that represent a rectangle"""
    def __init__(self,  width=0, height=0):
        """Initialize a rectangle instance.

        Args:
            width - width of the rectangle defaults to 0.
            height - height of the rectangle defaults to 0.
        Raises:
            TypeError: If both width and heigt are not integers.
            ValueError: If the width and height are less than 0.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set he height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError:If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
