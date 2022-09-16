#!/usr/bin/python3
"""Module 3-is_kind_of_class.
Finds if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Finds if obj is an instance of a_class or a class"""
    return isinstance(obj, a_class)
