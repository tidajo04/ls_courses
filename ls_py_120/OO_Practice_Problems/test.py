# # class Dog:
# #     def __init__(self, name, age):
# #         self._name = name
# #         self._age = age
    
# #     def bark(self):
# #         message = "Woof! Woof!"
# #         print(f'{message}')

# #     @property
# #     def name(self):
# #         return self._name
    
# #     @property
# #     def age(self):
# #         return self._age

# # fido = Dog('Fido', 5)
# # paws = Dog('Paws', 3)

# # print(fido.name)              # Fido
# # print(paws.name)              # Paws
# # print(fido.age)               # 5
# # print(paws.age)               # 3

# # fido.bark()                   # Woof! Woof!
# # paws.bark()                   # Woof! Woof!

# # try:
# #     fido.name = 'Barni'
# # except AttributeError as e:
# #     print(f"Error: {e}")      # prints error message

# # try:
# #     paws.age = 4
# # except AttributeError as e:
# #     print(f"Error: {e}")      # prints error message

# class SwimMixin:
#     def swim(self):
#         return "swims!"
    
# class Animal:
#     def __init__(self, legs=0):
#         self.legs = legs

#     def has_legs(self):
#         return f"This animal has {self.legs} legs"
    
# class Dog(Animal):
#     def __init__(self):
#         super().__init__(4)

#     def runs(self):
#         return "it runs on all fours!"

# class Fish(SwimMixin, Animal):
#     pass

# glip = Fish()
# fido = Dog()

# glip.skip()
# print(glip.swim())
# print(fido.has_legs())
# # print(fido.runs())

# class Dog():
#     def __init__(self, name):
#         self.name = name
#     #omitted extra code

# fido = Dog("Fido")
# ted = Dog("Ted")

# class Foo:
#     def __init__(self, bar, qux):
#         self._bar = bar
#         self._qux = qux

#     @property
#     def bar(self):
#         return self._bar
    
#     @bar.setter
#     def bar(self, new_bar):
#         if not isinstance (new_bar, int):
#             raise Exception
#         self._bar = new_bar

#     @property
#     def qux(self):
#         return self._qux
    

# foo = Foo(1, 2)

# print(foo.bar)      # 1
# foo.bar = 3
# print(foo.bar)      # 3
# print(foo.qux)      # 2

# try:
#     foo.qux = 4
# except AttributeError as e:
#     print(f"Error: {e}")      # prints an error message

# class Car:
#     def __init__(self, lumin):
#         self.lumin = lumin

#     @property
#     def lumin(self):
#         return self._speed

#     @lumin.setter
#     def lumin(self, value):
#         self._speed = value

#     def accelerate(self):
#         new_speed = self.lumin + 10
#         self.lumin = new_speed

#     def is_faster_than(self, other_car):
#         return self.lumin > other_car.lumin
    
    # def __eq__(self, other):
    #     return self.lumin == other.lumin

    # def __gt__(self, other):
    #     return self.lumin > other.lumin
    
    # def __lt__(self, other):
    #     return self.lumin < other.lumin
    

# Testing the Car class
# car1 = Car(40)
# car2 = Car(40)
# car1.accelerate()
# print(car1.is_faster_than(car2))

# class Person:
#     count = 0
#     def __init__(self):
#         Person.count += 1

#     @classmethod
#     def total_people(cls):
#         return cls.count

# bob = Person()
# alice = Person()
# print(Person.total_people())     # this should print 2

# 
# class ColorIntensity:
#     def __init__(self, lumin):
#         if not (0 <= lumin <= 255):
#             raise ValueError("Intensity must be between 0 and 255")
#         self.lumin = lumin
        
#     def __eq__(self, other):
#         return self.lumin == other.lumin

#     def __gt__(self, other):
#         return self.lumin > other.lumin
    
#     def __lt__(self, other):
#         return self.lumin < other.lumin

# ci1 = ColorIntensity(100)
# ci2 = ColorIntensity(150)
# ci3 = ColorIntensity(100)

# try:
#     ci4 = ColorIntensity(256)
# except ValueError as e:
#     print(f"Error: {e}")      # Prints an error message

# try:
#     ci5 = ColorIntensity(-1)
# except ValueError as e:
#     print(f"Error: {e}")      # Prints an error message

# print(ci1 < ci2)    # True
# print(ci1 == ci2)   # False
# print(ci3 == ci1)   # True
# print(ci3 > ci1)    # False
# print(ci2 > ci3)    # True

# class Counter:
#     def __init__(self):
#         self.count = 0

#     @property
#     def value(self):
#         return self.count

#     def increment(self, num):
#         self.count += num

#     def decrement(self, num):
#         self.count -= num

#     def __add__(self, other):
#         if isinstance(other, Counter):
#             return self.count + other.count
#         return NotImplemented
    
# c1 = Counter()
# c2 = Counter()
# c1.increment(3)
# c2.increment(5)
# c1.decrement(1)

# result = c1 + c2
# print(result)                 # 7

# try:
#     c1.value += 1
# except AttributeError as e:
#     print(f"Error: {e}")      # Prints error message

# try:
#     c1 = c1 + 1
# except TypeError as e:
#     print(f"Error: {e}")      # Prints error message

class FullTimeMixin:
    def take_vacation(self):
        pass #should decrement each employees remaining time

class Employee:
    def __init__(self, name, serial, hour_type):
        self.name = name
        self.serial = serial
        self.hour_type = hour_type
    
    def __str__(self):
        return (
        f"Name: {self.name} \n"
        f"Type: {self.__class__.__name__} \n"
        f"Serial number: {self.serial} \n"
        f"Vacation days: {self.vacation_remain} \n"
        f"Desk: {self.WORKSPACE}"
        )
    
class PartTimeEmployee(Employee):
    WORKSPACE = "None"

    def __init__(self, name, serial, hour_type):
        super().__init__(name, serial, hour_type)
        self.vacation_remain = 0
    
class RegularEmployee(FullTimeMixin, Employee):
    WORKSPACE = "cubicle Farm"
    
    def __init__(self, name, serial, hour_type):
        super().__init__(name, serial, hour_type)
        self.vacation_remain = 10
        
class Manager(FullTimeMixin, Employee):
    WORKSPACE = "private office"

    def __init__(self, name, serial, hour_type):
        super().__init__(name, serial, hour_type)
        self.vacation_remain = 14
    
    def delegate(self, employee_name):
        #ommitted code would instruct named employee what to do
        pass

class Executive(Manager):
    WORKSPACE = "corner office"

    def __init__(self, name, serial, hour_type):
        super().__init__(name, serial, hour_type)
        self.vacation_remain = 20

    def hire(self, name, serial, hour_type):
        #ommitted code would hire
        pass
    
    def fire(self, employee_name):
        #ommitted will fire employee
        pass

e = Executive("Dave", 123456789, "Full-Time")
print(e)

