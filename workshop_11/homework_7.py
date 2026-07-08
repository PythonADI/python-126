import math
class Shape:
    def __init__(self, tp):
        self.type = tp
    
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


shapes = []

with open("./workshop_11/shapes.txt") as f:
    for line in f:
        shape, data = line.split(",")
        if shape.lower() == "square":
            shapes.append(Square(float(data)))
        elif shape.lower() == "circle":
            shapes.append(Circle(float(data)))
        else:
            print(f"Shape {shape} does not exist in our program!")

for shape in shapes:
    print(shape)