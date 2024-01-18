#!/usr/bin/python3
"""This module provides methods for working with json"""
import json

"""This function creates an Object from a “JSON file”"""


def load_from_json_file(filename):
    """
    Creates an object to atext file from a json file.

    Parameters:
        _filename- the name of the file.

    Returns:
        -None
    """
    with open(filename) as json_file:
        return json.load(json_file)
