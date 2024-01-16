#!/usr/bin/python3
"""Creates a subclass that inherits from a superclass List"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
