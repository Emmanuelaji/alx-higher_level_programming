#!/usr/bin/python3
""" Module contains a function that returns an object(python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ Function that returns a pthon object represented by a json string
    Args:
        my_str: JSON string
    Raises:
        Exception: when string cant be decoded
    """
    return json.loads(my_str)
