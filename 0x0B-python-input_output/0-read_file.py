#!/usr/bin/python3
""" Module contains a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a file
    Args:
        filename: Name of file to be read
    Raises:
        Exception: Raises an exception when file cant be opened
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        readfile = f.read()
        print(readfile, end='')
