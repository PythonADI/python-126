import math


class Shape:
    @property
    def area(self):
        raise NotImplementedError()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


shapes: list[Shape] = [Rectangle(5, 5), Circle(3)]

for shape in shapes:
    print(shape.area)
