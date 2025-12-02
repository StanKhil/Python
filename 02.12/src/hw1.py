import math

class Figure:
    def area(self):
        return 0

class RectangleFigure(Figure):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def __int__(self):
        return int(self.area())
    def __str__(self):
        return f"RectangleFigure area={self.area()}"

class CircleFigure(Figure):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def __int__(self):
        return int(self.area())
    def __str__(self):
        return f"CircleFigure area={self.area()}"

class RightTriangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return 0.5 * self.a * self.b
    def __int__(self):
        return int(self.area())
    def __str__(self):
        return f"RightTriangle area={self.area()}"

class Trapezoid(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def area(self):
        return (self.a + self.b) * self.h / 2
    def __int__(self):
        return int(self.area())
    def __str__(self):
        return f"Trapezoid area={self.area()}"

class Shape:
    def Show(self):
        print(str(self))

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
    def __str__(self):
        return f"Square x={self.x} y={self.y} s={self.side}"

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def __str__(self):
        return f"Rectangle x={self.x} y={self.y} w={self.w} h={self.h}"

class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def __str__(self):
        return f"Circle x={self.x} y={self.y} r={self.r}"

class Ellipse(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def __str__(self):
        return f"Ellipse x={self.x} y={self.y} w={self.w} h={self.h}"

print("Task 1–2")
f1 = RectangleFigure(3, 4)
f2 = CircleFigure(3)
f3 = RightTriangle(3, 6)
f4 = Trapezoid(3, 5, 4)

print(int(f1), str(f1))
print(int(f2), str(f2))
print(int(f3), str(f3))
print(int(f4), str(f4))

print("Task 3 test")
s1 = Square(0, 0, 5)
s2 = Rectangle(1, 1, 4, 6)
s3 = Circle(2, 2, 7)
s4 = Ellipse(3, 3, 8, 4)

s1.Show()
s2.Show()
s3.Show()
s4.Show()
