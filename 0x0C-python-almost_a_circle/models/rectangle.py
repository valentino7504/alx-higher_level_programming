#!/usr/bin/python3
'''

This is a module that introduces a rectangle class

'''


from models.base import Base


class Rectangle(Base):
    """
    This is the rectangle class that inherits from base
    with width, height, x and y
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None) -> None:
        """
        Initialises a rectangle class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        validates and sets the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        returns x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        validates and sets the value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        returns the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        validates and sets the value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        gets the display string of the rectangle
        """
        rectangle_string = ""
        for _ in range(self.y):
            print()
        for i in range(self.height):
            rectangle_string += " " * self.x
            rectangle_string += "#" * self.width
            if i < self.height - 1:
                rectangle_string += "\n"
        print(rectangle_string)

    def update(self, *args, **kwargs):
        """
        updates the rectangle class
        """
        attributes = ["id", "width", "height", "x", "y"]
        set_attributes = []
        for new_value, attribute in zip(args, attributes):
            setattr(self, attribute, new_value)
            set_attributes.append(attribute)
        for attribute, new_value in kwargs.items():
            if attribute not in set_attributes:
                setattr(self, attribute, new_value)

    def __str__(self) -> str:
        """
        defines the string representation of the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.x}/" \
            f"{self.y} - {self.width}/{self.height}"
