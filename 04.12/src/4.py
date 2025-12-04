# import pickle
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self. age = age

#     def __str__(self):
#         return f"person {self.name} {self.age}"
    
# p = Person("tom", 23)
# with open("person.pkl", "wb") as file:
#     pickle.dump(p, file)
    
# with open("person.pkl", "rb") as file:
#     print(pickle.load(file))

import json
class Person:
    def __init__(self,name,age):
        self.name = name
        self. age = age

    def __str__(self):
        return f"person {self.name} {self.age}"
    
    def to_dict(self):
        return {"name": self.name, "age": self.age}
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
p = Person("tom", 23)

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(p.to_dict(), file, ensure_ascii=False, indent=4)

with open("data.json", "r", encoding="utf-8") as file:
    print(json.load(file))