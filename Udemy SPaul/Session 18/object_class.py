# Inheritance using Python.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Rectangle object width: {self.width}, height: {self.height}, area: {self.get_area()}, ' \
               f'Perimeter: {self.get_perimeter()}'


r = Rectangle(10, 4)
print(r.__str__())
print(issubclass(Rectangle, object))


