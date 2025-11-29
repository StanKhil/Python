class City:
    def __init__(self, name="", region="", country="", population=0, postind=0, phoneind=0 ) -> None:
        self.name = name
        self.region = region
        self.country = country
        self.__population = population
        self.postind = postind
        self.__phoneind = phoneind
    
    def __str__(self):
        return f"City Name: {self.name}, Region: {self.region}, Country: {self.country}, Population: {self.__population}, Post Index: {self.postind}, Phone Index: {self.__phoneind}"

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name


city1 = City("Los Angeles", "CA", "USA", 4000000, 1000001, 100)
print(city1)
city1.set_name("New York")
city1.region = "NY"
print(city1)