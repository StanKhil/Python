class Money:
    def __init__(self, num, type):
        self.num = num
        self.type = type

    def to_dolar(self, num=None, type=None):
        if num is None:
            num = self.num
        if type is None:
            type = self.type

        if type == "EUR":
            return num * 1.1
        elif type == "UAH":
            return num * 0.025
        else:
            return num

    def convert_to(self, new_type):
        dolar = self.to_dolar()

        if new_type == "EUR":
            self.num = dolar / 1.1
        elif new_type == "UAH":
            self.num = dolar / 0.025
        else:
            self.num = dolar

        self.type = new_type

    def __repr__(self):
        return f"{self.num:.2f} {self.type}"

    def __add__(self, other):
        if isinstance(other, Money):
            total = self.to_dolar() + other.to_dolar()
        else:
            total = self.to_dolar() + other
        return Money(total, "USD")

    def __radd__(self, other):
        return Money(self.to_dolar() + other, "USD")

    def __iadd__(self, other):
        if isinstance(other, Money):
            self.num = self.to_dolar() + other.to_dolar()
        else:
            self.num = self.to_dolar() + other

        self.type = "USD"
        return self

    def __mul__(self, other):
        return Money(self.to_dolar() * other, "USD")

    def __truediv__(self, other):
        return Money(self.to_dolar() / other, "USD")

    def __lt__(self, other):
        return self.to_dolar() < other.to_dolar()

    def __gt__(self, other):
        return self.to_dolar() > other.to_dolar()

    def __eq__(self, other):
        return self.to_dolar() == other.to_dolar()


a = Money(100, "EUR")
b = Money(1000, "UAH")
print(a + b)  # ~ 120 EUR
print(a * 3)  # 300 EUR

a.convert_to("USD")
print(a)    


