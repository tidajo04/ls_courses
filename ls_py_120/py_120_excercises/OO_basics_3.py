# ##PP1-2Inherited year

# class Vehicle:
#     def __init__(self, year):
#         self._year = year

#     @property
#     def year(self):
#         return self._year

# class Truck(Vehicle):

#     def __init__(self, year):
#         super().__init__(year)
#         self.start_engine()

#     def start_engine(self):
#         print('Ready to go!')

# class Car(Vehicle):
#     pass

# # Comments show expected output
# truck1 = Truck(1994)
# print(truck1.year)            # 1994

# car1 = Car(2006)
# print(car1.year)              # 2006

## PP3
# class Vehicle:
#     def __init__(self, year):
#         self._year = year

#     @property
#     def year(self):
#         return self._year

# class Truck(Vehicle):
#     def __init__(self, year, bed_type):
#         super().__init__(year)
#         self._bed_type = bed_type

#     @property
#     def bed_type(self):
#         return self._bed_type

# class Car(Vehicle):
#     pass

# # Comments show expected output
# truck1 = Truck(1994, 'Short')
# print(truck1.year)            # 1994
# print(truck1.bed_type)        # Short

# car1 = Car(2006)
# print(car1.year)              # 2006
# print(car1.bed_type)
# # AttributeError: 'Car' object has no attribute 'bed_type'

# PP4

# class Vehicle:
#     def start_engine(self):
#         return 'Ready to go!'

# class Truck(Vehicle):
#     def start_engine(self, speed):
#         self._speed = speed
#         return f'{super().start_engine()} Drive {self.speed}, please!'
    
#     @property
#     def speed(self):
#         return self._speed

# # Comments show expected output
# truck1 = Truck()
# print(truck1.start_engine('fast'))
# # Ready to go! Drive fast, please!

# truck2 = Truck()
# print(truck1.start_engine('slow'))
# # Ready to go! Drive slow, please!

## PP5
# class WalkingMixin:
#     def walk(self):
#         print('Let\'s go for a walk!')

# class Cat(WalkingMixin):
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def greet(self):
#         print(f"Hello! My name is {self.name}!")

# # Comments show expected output
# kitty = Cat('Sophie')
# kitty.greet()       # Hello! My name is Sophie!
# kitty.walk()        # Let's go for a walk!
## PP6

# class TowingMixin:
#     def tow(self):
#         return 'I can tow a trailer!'
    
# class Vehicle:
#     def __init__(self, year):
#         self.year = year

# class Truck(Vehicle, TowingMixin):
#     pass

# class Car(Vehicle):
#     pass

# # Comments show expected output
# truck1 = Truck(1994)
# print(truck1.year)            # 1994
# print(truck1.tow())           # I can tow a trailer!

# car1 = Car(2006)
# print(car1.year)              # 2006

# PP8
# class FlyingMixin:
#     def fly(self):
#         return "I'm flying!"

# class Animal:
#     def __init__(self, color):
#         self._color = color

#     @property
#     def color(self):
#         return self._color

# class Cat(Animal):
#     pass

# class Bird(FlyingMixin, Animal):
#     pass

# bird1 = Bird('Red')
# print(bird1.color)

class Person:
    def __init__(self, name):
        self.name = name

bob = Person("Robert")

print(bob.__dict__)  # {'name': 'Robert'}


