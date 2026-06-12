import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplemented
    
    def perimeter(self):
        raise NotImplemented

class Square(Shape):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    def area(self):
        return self.size * self.size

    def perimeter(self):
        return self.size * 2


class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.radius * math.pi

things = [Square("sq", 2), Circle("ci", 4)]

for th in things:
    name = th.name
    area = th.area()
    perimeter = th.perimeter()
    print(f"This is a {name} with area {area} and perimeter {perimeter}")
