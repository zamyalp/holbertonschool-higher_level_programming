#!/usr/bin/python3
"""Module 10-student"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initializer method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dictionary representation of
        student instance
        """
        dict = vars(self)
        if attrs is None:
            return dict

        studentInfo = {}
        for item in attrs:
            if item in dict:
                studentInfo[item] = dict[item]
        return studentInfo
