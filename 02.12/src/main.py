# class Car:
#     def __init__(self,model=None, year=0, vin=None ) -> None:
#         self.model = model
#         self.year = year
#         self.vin = vin

#     def __str__(self):
#         return f"Model: {self.model}, Year: {self.year}, VIN: {self.vin}"
    
#     @classmethod
#     def from_string(cls, car_string):
#         model, year, vin = car_string.split("-")
#         return cls(model, int(year), vin)
    
#     @classmethod
#     def from_vin(cls, vin):
#         return cls("", 0, vin)
    
#     @classmethod
#     def from_dict(cls, car_dict):
#         return cls(car_dict["model"], car_dict["year"], car_dict["vin"])

#     @property
#     def model(self):
#         return self.__model
    
#     @model.setter
#     def model(self, value):
#         self.__model = value
    

# class Country:
#     def __init__(self, name="", continent="", phone=0, capital="", population=0, area=0, cities=[]) -> None:
#         self.name = name
#         self.population = population
#         self.area = area
#         self.cities = cities
#         self.continent = continent
#         self.phone = phone
#         self.capital = capital

#     def __str__(self):
#         return f"Country: {self.name}, Continent: {self.continent}, Phone Code: {self.phone}, Capital: {self.capital}, Population: {self.population}, Area: {self.area}, Cities: {', '.join(self.cities)}"
    
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, value):
#         self.__name = value
#     @property
#     def population(self):
#         return self.__population
#     @population.setter
#     def population(self, value):
#         self.__population = value   
#     @property
#     def area(self):
#         return self.__area
#     @area.setter
#     def area(self, value):
#         self.__area = value
#     @property
#     def cities(self):
#         return self.__cities
#     @cities.setter
#     def cities(self, value):
#         self.__cities = value
#     @property
#     def continent(self):
#         return self.__continent
#     @continent.setter
#     def continent(self, value):
#         self.__continent = value

#     @classmethod
#     def from_string(cls, country_string):
#         name, continent, phone, capital, population, area, cities = country_string.split("-")
#         cities_list = cities.split(",") if cities else []
#         return cls(name, continent, int(phone), capital, int(population), int(area), cities_list)
#     @classmethod
#     def from_dict(cls, country_dict):
#         return cls(country_dict["name"], country_dict["continent"], country_dict["phone"], country_dict["capital"], country_dict["population"], country_dict["area"], country_dict["cities"])

# city1 = Country.from_string("Utopia-Europe-123-PerfectCity-1000000-50000-CityA,CityB,CityC")
# print(city1)
# city2 = Country.from_dict({"name": "Dystopia", "continent": "Asia", "phone": 456, "capital": "DarkCity", "population": 2000000, "area": 75000, "cities": ["CityX", "CityY"]})
# print(city2)

class Animal:
    def __init__(self, name) -> None:
        self.name = name
        print("animal base constructor")
    def speak(self):
        pass

class Feline:
    def meow(self):
        return "meow!"

class Cat(Animal,Feline):
    def speak(self):
        return f"{self.name} says Mew"

cat = Cat("vasya")
print(cat.speak())
print(cat.meow())
