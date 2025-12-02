class Device:
    def __init__(self, firm, power):
        self.firm = firm
        self.power = power
    def info(self):
        return f"{self.brand} {self.power}W"


class CoffeeMachine(Device):
    def __init__(self, firm, power, pressure):
        super().__init__(firm, power)
        self.pressure = pressure
    def make_coffee(self):
        print("Coffee ready")
    def info(self):
        return f"CoffeeMachine {self.firm} {self.power}W {self.pressure}bar"


class Blender(Device):
    def __init__(self, firm, power, speed):
        super().__init__(firm, power)
        self.speed = speed
    def blend(self):
        print("Blending")
    def info(self):
        return f"Blender {self.firm} {self.power}W speed:{self.speed}"


class MeatGrinder(Device):
    def __init__(self, firm, power, capacity):
        super().__init__(firm, power)
        self.capacity = capacity
    def grind(self):
        print("Grinding")
    def info(self):
        return f"MeatGrinder {self.firm} {self.power}W {self.capacity}kg/min"


class Ship:
    def __init__(self, name, crew):
        self.name = name
        self.crew = crew
    def info(self):
        return f"{self.name} crew:{self.crew}"


class Frigate(Ship):
    def __init__(self, name, crew, missiles):
        super().__init__(name, crew)
        self.missiles = missiles
    def attack(self):
        print("Frigate attack")
    def info(self):
        return f"Frigate {self.name} crew:{self.crew} missiles:{self.missiles}"


class Destroyer(Ship):
    def __init__(self, name, crew, guns):
        super().__init__(name, crew)
        self.guns = guns
    def fire(self):
        print("Destroyer fire")
    def info(self):
        return f"Destroyer {self.name} crew:{self.crew} guns:{self.guns}"


class Cruiser(Ship):
    def __init__(self, name, crew, armor):
        super().__init__(name, crew)
        self.armor = armor
    def defend(self):
        print("Cruiser in rush")
    def info(self):
        return f"Cruiser {self.name} crew:{self.crew} armor:{self.armor}"


class Money:
    def __init__(self, whole=0, cents=0):
        self.set_value(whole, cents)

    def set_value(self, whole, cents):
        self.whole = whole
        self.cents = cents % 100
        self.whole += cents // 100

    def show(self):
        print(f"{self.whole}.{self.cents}")


class Product:
    def __init__(self, name, price: Money):
        self.name = name
        self.price = price

    def discount(self, amount):
        cents = self.price.whole * 100 + self.price.cents
        cents -= int(amount * 100)
        if cents < 0:
            cents = 0
        self.price.set_value(cents // 100, cents % 100)

    def info(self):
        return f"{self.name} price:{self.price.whole}.{str(self.price.cents).zfill(2)}"


print("Task 1")
c = CoffeeMachine("Philips", 1500, 15)
b = Blender("Bosch", 800, 5)
m = MeatGrinder("Tefal", 1200, 2)

print(c.info())
print(b.info())
print(m.info())

c.make_coffee()
b.blend()
m.grind()

print("Task 2")
f = Frigate("Frigate", 120, 16)
d = Destroyer("Destroyer", 200, 4)
cr = Cruiser("Cruiser", 350, 200)
print(f.info())
print(d.info())
print(cr.info())
f.attack()
d.fire()
cr.defend()

print("Task 3")
money = Money(5, 75)
p = Product("Milk", money)
print(p.info())
p.discount(1.30)
print(p.info())
money.show()
