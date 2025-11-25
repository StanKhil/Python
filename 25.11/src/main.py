countries = {'GB': 'London', 'France': 'Paris', 'Germany': 'Berlin', 'RSA': ('Pretoria','Cape Town','Bloemfontein')}

#CREATE
country ="Ukraine"
capital = "Kyiv"
countries[country] = capital
print(countries)

#READ
print(countries)
for country, capital in countries.items():
    print(f"The capital of {country:20} is {capital}")

#UPDATE
country = "Germany"
capital = "Bonn"
if country in countries:
    countries[country] = capital

#DELETE
country = "France"
if country in countries:
    del countries[country]
print(countries)

#FIND
country = "Germany"
if country in countries:
    print(f"The capital of {country} is {countries[country]}")
else:
    print(f"{country} not found")

#REPLACE (key)
old_country = "Germany"
new_country = "4Reich"
if old_country in countries:
    countries[new_country] = countries.pop(old_country)
print("Replaced", countries)