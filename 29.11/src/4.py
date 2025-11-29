class Car:
    name = "Default"
    model = "Default"
    year = 2000
    vin = "0000000000"

    def __str__(self) -> str:
        return f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}, VIN: {self.vin}"
    
car1 = Car()
car2 = Car()

car1.name = "Audi"
car1.year = 2022
print(car1)
print(car2)
Car.year = 2025
print(car1)
print(car2)