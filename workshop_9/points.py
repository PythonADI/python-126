class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    
a, b, c = Point(3, 7), Point(3, 7), Point(9, 0)

print(a == b)
print(a is b)
print(id(a))
print(id(b))