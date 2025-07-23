# # CH Object Model 
# # ex. 1
# # class OfficeSupplies:
    
# #     def __init__(self, name):
# #         self.name = name

# # scissors = OfficeSupplies('Scissors')
# # pencils = OfficeSupplies('Pencils')

# # ex.2
# # class Foo:
# #     pass

# # foo = Foo()
# # print(f'I am a {type(foo).__name__} object')
# # print(f'I am a {foo.__class__.__name__} object')

# # CH Classes and Objects
# # ex 1. 
# class Car:

#     def __init__(self, name, model, year, color):
#         self.current_speed = 0
#         self.current_state = "Off"
#         self._model = model
#         self._year = year
#         self._color = color
#         self._name = name
#         print(f'The {color}, {year}, {name} {model} has entered the race')

#     @property
#     def model(self):
#         return self._model
    
#     @property
#     def year(self):
#         return self._year
    
#     @property
#     def color(self):
#         return self._color
    
#     @color.setter
#     def color(self, color):
#         if not isinstance(color, str):
#             raise TypeError('Color must be a string')

#         self._color = color

#     def __str__(self):
#         return f'{self._color} {self._name}' 
    
#     def speed(self):
#         if self.current_speed > 0:
#             print(f'The {self} is moving at {self.current_speed} mph.')
#         else:
#             print(f'The {self} isn\'t moving')

#     def engine_on(self):
#         if self.current_state == "Off":
#             self.current_state = "On"
#             print(f'The {self} starts its engine!')
#         else:
#             print(f'The car is already running')
        
#     def accelerate(self, speed):
#         if self.current_state == "On":
#             self.current_speed += speed
#             print(f'The {self} speeds up!')
#         else:
#             print("The car is not running. You must start your engine!")

#     def brake(self, slow):
        
#         if self.current_speed > 0:
#             self.current_speed = max(self.current_speed - slow, 0)
#             print(f'The {self} hits the brakes, reducing its speed to {self.current_speed}')
            
#         else:
#             print('The car is already at a complete stop')

#     def engine_off(self):
#         if self.current_state == "On" and self.current_speed == 0:
#             self.current_state = "Off"
#             print(f'The {self} powers down!')
#         else:
#             if self.current_state == "Off":
#                 print("The engine is already off")
#             if self.current_speed > 0:
#                 print("You must brake to a stop before cutting your engine!")
    
#     def paint_job(self, new_color):
#         self._color = new_color
#         print(f'The {self._name} has been painted {new_color}')

#     @classmethod
#     def mileage(cls, gallons, miles):
#         mileage = miles / gallons
#         print(f'{mileage} miles per gallon')

# # class Person:

# #     def __init__(self, first_name, last_name):
# #         self._set_name(first_name, last_name)

# #     @property
# #     def name(self):
# #         first_name = self._first_name.title()
# #         last_name = self._last_name.title()
# #         return f'{first_name} {last_name}'
    
# #     @name.setter
# #     def name(self, name):
# #         first_name, last_name = name
# #         self._set_name(first_name, last_name)

# #     @classmethod
# #     def _validate(cls, name):
# #         if not name.isalpha():
# #             raise ValueError('Name must be alpha chars only.')
    
# #     def _set_name(self, first_name, last_name):
# #         Person._validate(first_name)
# #         Person._validate(last_name)
# #         self._first_name = first_name
# #         self._last_name = last_name

# # actor = Person('Mark', 'sinclair')
# # print(actor.name)              # Mark Sinclair
# # actor.name = ('Vin', 'Diesel')
# # print(actor.name)              # Vin Diesel
# # actor.name = ('', 'Diesel')
# # # ValueError: Name must be alphabetic.

# # character = Person('annIE', 'HAll')
# # print(character.name)          # Annie Hall
# # character = Person('Da5id', 'Meier')
# # # ValueError: Name must be alphabetic.

# # friend = Person('Lynn', 'Blake')
# # print(friend.name)             # Lynn Blake
# # friend.name = ('Lynn', 'Blake-John')
# # # ValueError: Name must be alphabetic.
# # mazda = Car('Mazda', 'CX9', 2000, 'blue')
# # Car.mileage(10, 200)
# # mazda.color = 'white'
# # print(mazda.color)
# # print(mazda.model)

# # mazda.speed()
# # mazda.engine_off()
# # mazda.engine_on()
# # mazda.accelerate(23)
# # mazda.speed()
# # mazda.brake(20)
# # mazda.speed()
# # mazda.brake(10)
# # mazda.speed()
# # mazda.brake(10)
# # mazda.engine_on()
# # mazda.accelerate(40)
# # mazda.engine_off()
# # mazda.brake(40)
# # mazda.engine_off()

# # ford = Car('Ford', 'F150', 2012, 'black')
# # print(ford.color)
# # ford.color = 'grey'
# # print(ford.color)
# # print(ford.year)
# # ford.speed()

# # mazda.paint_job('red')
# # John = Person('John', 'Smith') 

# class Cat:

#     def __init__(self, name):
#         self.name = [name]

#     def __str__(self):
#         return self.name

#     def __repr__(self):
#         return f'Cat({repr(self.name)})'

# cat = Cat('Fuzzy')
# # print(cat)  # Fuzzy
# print(repr(cat)) # Cat('Fuzzy')
# import os

# print(__file__)
# print(os.path.abspath(__file__))
# assets = os.path.abspath(f'{__file__}/../assets')
# print(assets)

# image = f'{assets}/foo.png'
# print(image)

# class Car:
    
#     def __init__(self, model, year, color):
#         self._model = model
#         self._year = year
#         self._color = color

#     def __str__(self):
#         return f'{self._color.title()} {self._year} {self._model}'

#     def __repr__(self):
#         color = repr(self._color)
#         year = repr(self._year)
#         model = repr(self._model)
#         return f'Car({model}, {year}, {color})'

# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)
    
#     def __sub__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         new_x = self.x - other.x
#         new_y = self.y - other.y
#         return Vector(new_x, new_y)
    
#     def __mul__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         new_x = self.x * other.x
#         new_y = self.y * other.y
#         return new_x + new_y
    
#     def abs(self):
#         return abs(self.x, self.y)
    
    

#     # __iadd__ method omitted; we don't need it for this exercise

#     def __repr__(self):
#         x = repr(self.x)
#         y = repr(self.y)
#         return f'Vector({x}, {y})'

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)      # Vector(18, 8)
# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0

# class Car:

#     def __init__(self, id, year, color):
#         self.id = id
#         self.year = year
#         self.color = color.title()

#     def __str__(self):
#         return f'{self.color} {self.year} {self.id}'
        
#     def __repr__(self):
#         return (f"Car({repr(self.color)} {repr(self.year)} {repr(self.id)})")
        
# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')    

# import math

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)

#     def __sub__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x - other.x
#         new_y = self.y - other.y
#         return Vector(new_x, new_y)

#     def __mul__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         dot_product = ((self.x * other.x) +
#                         (self.y * other.y))
#         return dot_product

#     def __abs__(self):
#         sum_of_squares = ((self.x ** 2) +
#                           (self.y ** 2))
#         return math.sqrt(sum_of_squares)

#     def __repr__(self):
#         x = repr(self.x)
#         y = repr(self.y)
#         return f'Vector({x}, {y})'

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)      # Vector(18, 8)
# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0
# class Candidate:

#     def __init__(self, name):
#         self.name = name
#         self.votes = 0

#     def __iadd__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented

#         self.votes += other
#         return self

# class Election:

#     def __init__(self, candidates):
#         self.candidates = candidates

#     def results(self):
#         max_votes = 0
#         vote_count = 0
#         winner = None

#         for candidate in self.candidates:
#             vote_count += candidate.votes
#             if candidate.votes > max_votes:
#                 max_votes = candidate.votes
#                 winner = candidate.name

#         for candidate in self.candidates:
#             name = candidate.name
#             votes = candidate.votes
#             print(f'{name}: {votes} votes')

#         percent = 100 * (max_votes / vote_count)
#         print()
#         print(f'{winner} won: {percent}% of votes')
        
    


# mike_jones = Candidate('Mike Jones')
# susan_dore = Candidate('Susan Dore')
# kim_waters = Candidate('Kim Waters')

# candidates = [
#     mike_jones,
#     susan_dore,
#     kim_waters,
# ]

# votes = [
#     mike_jones,
#     susan_dore,
#     mike_jones,
#     susan_dore,
#     susan_dore,
#     kim_waters,
#     susan_dore,
#     mike_jones,
# ]

# for candidate in votes:
#     candidate += 1

# election = Election(candidates)
# election.results()
# class Vehicle:
#     def __init__(self, wheels):
#         self.wheels = wheels
#         print(f'creating a {self.__class__.__name__}')
#         print(f'I have {self.wheels} wheels.')

#     # def __str__(self):
#     #     return self.__class__.__name__
    
#     def drive(self):
#         print('I am driving.')

# class Car(Vehicle):
#     pass
#     # def __init__(self):
#     #     print('Creating a car.')
#     #     super().__init__(4)

# class Truck(Vehicle):
#     pass
#     # def __init__(self):
#     #     print('Creating a truck.')
#     #     super().__init__(18)

# class Motorcycle(Vehicle):
#     pass
#     # def __init__(self):
#     #     print('Creating a motorcycle.')
#     #     super().__init__(2)
    
#     def drive(self):
#         super().drive()
#         print('No, I am riding!')

# car = Car(4)
# car.drive()               # I am driving.

# truck = Truck(18)
# truck.drive()             # I am driving.

# motorcycle = Motorcycle(2)
# motorcycle.drive()  # I am driving.

# class Pet:

#     def play(self):
#         print('I am playing')

#     def eat(self):
#         print('I eat kibble')

# class Preditor:

#     def hunt(self):
#         print('I am hunting')
    
#     def eat(self):
#         print('I eat prey')

# class Cat(Pet, Preditor):

#     def purr(self):
#         print('I am purring')

# cat = Cat()
# cat.purr()
# cat.play()
# cat.hunt()
# Preditor.eat(cat)
# class ColorMixin:

#     def set_color(self, color):
#         self._color = color
    
#     def get_color(self):
#         return self._color
    
# class Car(ColorMixin):

#     def __init__(self, color):
#         self.set_color(color)
    
# class House(ColorMixin):

#     def __init__(self, color):
#         self.set_color(color)

# class SmartLight(ColorMixin):

#     def __init__(self, color):
#         self.set_color(color)



# smart_light = SmartLight('cool white')
# print(smart_light.get_color())   # cool white

# smart_light.set_color('goldenrod')
# print(smart_light.get_color())   # goldenrod

# house = House('sky blue')
# print(house.get_color())         # sky blue

# house.set_color('lavender')
# print(house.get_color())         # lavender

# car = Car('red')
# print(car.get_color())

# car.set_color('green')
# print(car.get_color())

# class SignalMixins:

#     def signal_left(self):
#         print('Signalling left')

#     def signal_right(self):
#         print('Signalling right')

#     def signal_off(self):
#         print('Signal is now off')

# class Vehicle:

#     number_of_vehicles = 0

#     def __init__(self):
#         Vehicle.number_of_vehicles += 1

#     @classmethod
#     def vehicles(cls):
#         return Vehicle.number_of_vehicles

# class Car(Vehicle, SignalMixins):

#     def __init__(self):
#         super().__init__()

# class Truck(Vehicle, SignalMixins):

#     def __init__(self):
#         super().__init__()

# class Boat(Vehicle, SignalMixins):

#     def __init__(self):
#         super().__init__()

# print(Car.vehicles())     # 0
# car1 = Car()
# print(Car.vehicles())     # 1
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.vehicles())     # 4
# truck1 = Truck()
# truck2 = Truck()
# print(Truck.vehicles())   # 6
# boat1 = Boat()
# boat2 = Boat()
# print(Boat.vehicles())    # 8

# car1.signal_left()       # Signalling left
# truck1.signal_right()    # Signalling right
# car1.signal_off()        # Signal is now off
# truck1.signal_off()      # Signal is now off
# boat1.signal_left()
# # AttributeError: 'Boat' object has no attribute
# # 'signal_left'

# print(Car.mro())
# class Vehicle:
#     def __init__(self, fuel_capacity, mpg):
#         self.capacity = fuel_capacity
#         self.mpg = mpg

#     def max_range_in_miles(self):
#         return self.capacity * self.mpg
    
# class Car(Vehicle):

#     def __init__(self, fuel_capacity, mpg):
#         super().__init__(fuel_capacity, mpg)

#     def family_drive(self):
#         print('Taking the family for a drive')

# class Truck(Vehicle):

#     def __init__(self, fuel_capacity, mpg):
#         super().__init__(fuel_capacity, mpg)

#     def hookup_trailer(self):
#         print('Hooking up trailer')

# car = Car(12.5, 25.4)
# truck = Truck(150.0, 6.25)

# print(car.max_range_in_miles())         # 317.5
# print(truck.max_range_in_miles())       # 937.5

# car.family_drive()     # Taking the family for a drive
# truck.hookup_trailer() # Hooking up trailer

# try:
#     truck.family_drive()
# except AttributeError:
#     print('No family_drive method for Truck')
# # No family_drive method for Truck

# try:
#     car.hookup_trailer()
# except AttributeError:
#     print('No hookup_trailer method for Car')
# # No hookup_trailer method for Car