#!/usr/bin/python3
"""This is the documentation for my_module.

It provides a brief overview of the module's purpose and functionality.
"""


class Square:
    """A class that represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance with size and position.

        Args:
            size: size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        Raises:
            TypeError: If size is not an integer, or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0, or position contains non-positive integers.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(val, int) for val in position) or not all(val >= 0 for val in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(val, int) for val in value) or \
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
