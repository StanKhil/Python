class My_Math:
    @staticmethod
    def Add(a, b):
        return a + b
    
    @staticmethod
    def Subtract(a, b):
        return a - b
    
p = My_Math().Add(10, 5)
q = My_Math().Subtract(10, 5)
# print(p)
# print(q)

class CarWithCounter:
    __count_cars = 0

    def __init__(self, name="", model=None, year=0, vin=None ) -> None:
        self.name = name
        self.model = model
        self.year = year
        self.vin = vin
        CarWithCounter.__count_cars += 1

    @staticmethod
    def GetCountCars():
        return CarWithCounter.__count_cars
    

car1 = CarWithCounter("Toyota", "Camry", 2021, "JT4")
car2 = CarWithCounter("Toyota", "Camry", 2021, "JT4")
car3 = CarWithCounter("Toyota", "Camry", 2021, "JT4")

print(CarWithCounter.GetCountCars())
print(car3.__count_cars)