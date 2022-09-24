#!/usr/bin/python3
"""
    class that inherits base.
"""


from models.base import Base


class Rectangle(Base):
    """Inherited class that attributes to rectangles"""

    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor and initiation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints the Rectangle instance with #"""
        for y_axis in range(0, self.__y):
            print()
        for column in range(0, self.__height):
            string = ''
            for x_axis in range(0, self.__x):
                string = string + ' '
            for row in range(0, self.__width):
                string = string + '#'
            print(string)

    def __str__(self):
        """Using str method to return a message"""
        message = "[Rectangle] ({}) ".format(self.id, end='')
        message2 = "{}/{} ".format(self.x, self.y, end='')
        message3 = "- {}/{}".format(self.width, self.height)
        return message + message2 + message3

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args is not None and len(args) > 0:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.width = arg
                if count == 2:
                    self.height = arg
                if count == 3:
                    self.x = arg
                if count == 4:
                    self.y = arg
                count = count + 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Using dictionary representation"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
