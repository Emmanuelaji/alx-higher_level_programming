#!/usr/bin/python3
""" Module contains a function that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Function that creates and object from JSON file
    Args:
        filename: JSON to decode
    Raises:
        Exception: when file cannot be decoded
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
