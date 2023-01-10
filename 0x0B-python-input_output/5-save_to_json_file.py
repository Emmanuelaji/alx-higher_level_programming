#!/usr/bin/python3
""" Module contains function that writes an object to a text file,
using JON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that encodes an object to a file
    Args:
        filename: textfile name
        my_obj: object
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
