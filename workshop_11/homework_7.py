import math
class Shape:
    def __init__(self, type):
        self.type = type
    
    @property
    def area(self):
        raise NotImplementedError()
    
    def __str__(self):
        return f"{self.type} - {self.area} with area"

class Square(Shape):
    def __init__(self, side):
        super().__init__(self.__class__.__name__)
        self.side = side
    
    @property
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, r):
        super().__init__("Circle")
        self.radius = r
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)


square = Square(5)
c = Circle(7)

print(square)
print(c)