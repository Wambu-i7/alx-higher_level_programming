#!/usr/bin/python3
"""Creates a subclass that inherits from a superclass List"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))    
