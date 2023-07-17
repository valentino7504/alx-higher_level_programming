#!/usr/bin/python3
'''

A square module for 0x0C project on almost a circle

'''


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a square class that inherits from the Rectangle class
    """
    def __init__(self, size: int, x=0, y=0, id=None) -> None:
        """
        Init for square class
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        the size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the value of size
        """
        self.width = value
        self.__size = self.width
        self.height = self.__size

    def __str__(self) -> str:
        """
        __str__ for square class
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
