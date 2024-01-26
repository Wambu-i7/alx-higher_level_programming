#!/usr/bin/python3
"""Defining a class base"""


class Base:
    """
    Base class to manage id attribute for all future classes in the project.

    Attributes:
        __nb_objects (int): Private class attribute.
        id (int): Public instance attribute represent the unique
        identifier for each instance.

    Methods:
        __init__(self, id=None): Class constructor to initialize id attribute.
    """
    __nb_objects = 0
    """
        Initialize Base instance with a unique identifier.

        Args:
            id (int, optional): Identifier for the instance.
        """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """
    Rectangle class representing a rectangle shape.

    Inherits from Base class.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle's position.
        y (int): y-coordinate of the rectangle's position.
        id (int): Unique identifier of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Class constructor.
        area(self): Calculate the area of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle instance with specified attributes.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle (default is 0).
            y (int, optional): y-coordinate of the rectangle (default is 0).
            id (int, optional): Unique identifier of the rectangle..

        Note:
            If id not provided,will be automatic assigned by the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.width * self.height
