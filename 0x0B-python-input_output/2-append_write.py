#!/usr/bin/python3
""" Module contains a function that appends a string to a text file """


def append_write(filename="", text=""):
    """ Function that append to a file
    Args:
        filename: name of file to append text
        text: text to append to file
    Raises:
        exception: raises an exception if file can't be opened
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
