#!/usr/bin/python3
"""Module 9-student"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initializer method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
       """
       retrieves dictionary representation of
       student instance
       """
       return vars(self)
