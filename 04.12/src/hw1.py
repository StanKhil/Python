import math

class Circle:
    def __init__(self, r):
        self.r = r

    def length(self):
        return 2 * math.pi * self.r

    def __eq__(self, other):
        return self.r == other.r

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __add__(self, other):
        return Circle(self.r + other)

    def __sub__(self, other):
        return Circle(self.r - other)

    def __iadd__(self, other):
        self.r += other
        return self

    def __isub__(self, other):
        self.r -= other
        return self

    def __repr__(self):
        return f"Circle({self.r})"


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b,
                       self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        d = other.a * other.a + other.b * other.b
        return Complex((self.a * other.a + self.b * other.b) / d,
                       (self.b * other.a - self.a * other.b) / d)

    def __repr__(self):
        return f"{self.a}+{self.b}i"


class Airplane:
    def __init__(self, type, seats, passengers):
        self.type = type
        self.seats = seats
        self.passengers = passengers

    def __eq__(self, other):
        return self.type == other.type

    def __add__(self, other):
        return Airplane(self.type, self.seats, self.passengers + other)

    def __sub__(self, other):
        return Airplane(self.type, self.seats, self.passengers - other)

    def __iadd__(self, other):
        self.passengers += other
        return self

    def __isub__(self, other):
        self.passengers -= other
        return self

    def __lt__(self, other):
        return self.passengers < other.passengers

    def __le__(self, other):
        return self.passengers <= other.passengers

    def __gt__(self, other):
        return self.passengers > other.passengers

    def __ge__(self, other):
        return self.passengers >= other.passengers

    def __repr__(self):
        return f"{self.type} ({self.passengers}/{self.seats})"


class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __repr__(self):
        return f"{self.area}m*m {self.price}$"
