class Car:
    name = ""
    model = ""
    year = 0
    vin = ""

    def __init__(self, name="", model=None, year=0, vin=None ) -> None:
        self.name = name
        self.model = model
        self.year = year
        self.vin = vin
    

    def PrintCar(self):
        print(f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}, VIN: {self.vin}")

    def __str__(self):
        return f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}, VIN: {self.vin}"

    def InitCar(self, name, model, year, vin):
        self.name = name
        self.model = model
        self.year = year
        self.vin = vin

    def __del__(self):
        print(f"Car {self.name} is being deleted.")

car1 = Car()
car1.model = "BMV"
car1.InitCar("BMV", "X5", 2020, "1HGCM82633A123456")
print(car1)