#!/usr/bin/python3
    """
    Reads the content of a text file (UTF-8) and prints it to stdout.

    Parameters:
    - filename (str): The name of the text file to be read. Default is an empty string.

    Returns:
    None
    """


def read_file(filename=""):
    """ Reads the content of a text file (UTF-8) and prints it to stdout."""
    with open(filename, mode='r', encoding='utf-8') as rfile:
        print(rfile.read())
