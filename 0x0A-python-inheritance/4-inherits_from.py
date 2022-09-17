#!/usr/bin/python3
"""Module 4-inherits_from.
Finds if the object is an instance of a class that inherited
(directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """Determines if obj is an instance of a class that inherited from a_class"""
    return issubclass(type(obj), a class) and type(obj) != a_class
