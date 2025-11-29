class Car:
    def __init__(self, name="", model=None, year=0, vin=None ) -> None:
        self.name = name
        self.model = model
        self.year = year
        self.vin = vin

    def __str__(self):
        return f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}, VIN: {self.vin}"

class Book:
    def __init__(self, title="", author=None, year=0, isbn=None ) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self):
        return f"Book Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}"
    
class Stadium:
    def __init__(self, name="", location=None, capacity=0, built_year=0 ) -> None:
        self.name = name
        self.location = location
        self.capacity = capacity
        self.built_year = built_year

    def __str__(self):
        return f"Stadium Name: {self.name}, Location: {self.location}, Capacity: {self.capacity}, Built Year: {self.built_year}"
    
class Fraction:
    __count_fractions = 0

    def __init__(self, numerator=0, denominator=1) -> None:
        self.numerator = numerator
        self.denominator = denominator
        Fraction.__count_fractions += 1

    def __str__(self):
        return f"Fraction: {self.numerator}/{self.denominator}"
    
    @staticmethod
    def get_count_fractions():
        return Fraction.__count_fractions

class Converter:
    __temp_counter = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        Converter.__temp_counter += 1
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        Converter.__temp_counter += 1
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def get_temp_counter():
        return Converter.__temp_counter
    
class DistanceConverter:
    @staticmethod
    def km_to_miles(km):
        return km * 0.621371
    
    @staticmethod
    def miles_to_km(miles):
        return miles / 0.621371  
    
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084
    
    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084
    