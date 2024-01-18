#!/usr/bin/python3
"""This module provides methods for working with json"""
import json

"""This function writes an Object to a text file, using a JSON"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to atext file using json.

    Parameters:
        -my_obj - object to be written in text file.
        _filename- the name of the file.

    Returns:
        -None
    """
    with open(filename, 'w') as py_file:
        json.dump(my_obj, py_file)
