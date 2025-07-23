# class Dog:
#     def __init__(self, breed):
#         self._breed = breed

#     def get_breed(self):
#         return self._breed

# cuddles = Dog('Golden Retriever')
# butch = Dog('Poodle')

# class Cat:
#     def get_name(self):
#         try:
#             return self.name
#         except AttributeError:
#             return "Name not set!"

# # print(cuddles._breed)
# # print(butch._breed)
# # print(cuddles.get_breed())
# # print(butch.get_breed())
# # pinky = Cat()

# # print(pinky.get_name())
# # pinky.name = "Pinky"
# # print(pinky.get_name())

# butch._breed = "lab"
# print(butch.get_breed())

# class Student:
#     school_name = "oxford"

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def get_school_name(cls):
#         return cls.school_name

# # tom = Student('Tom')
# # bill = Student('Bill')
# # print(tom.name, tom.__class__.school_name)
# # print(bill.name, bill.__class__.school_name)
# print(Student.school_name)
# print(Student.get_school_name())

# class Car:
#     manufacturer = "A"
#     def __init__(self):
#         self.manufacturer = 'B'

#     def show_manufacturers(self):
#         print(self.__class__.manufacturer)
#         print(self.manufacturer)

# car1 = Car()
# car1.show_manufacturers()

# class Mammal:
#     LEGS = 4

# class Human(Mammal):
#     LEGS = 2

# print(Human.LEGS)
