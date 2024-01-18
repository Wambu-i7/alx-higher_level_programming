#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """ Writes contents on a text file and returns numberof characters
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as rfile:
        return rfile.write(text)
