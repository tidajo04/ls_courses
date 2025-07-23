# PP1 BANNER CLASS
# class Banner:
#     def __init__(self, message, width):
#         if width >= len(message):
#             self.width = width
#         else: 
#             print('Note: message exceeds minimum width requrements,' \
#             'defaulting to message length')
#             self.width = len(message) + 2
            
#         self.message = message

        

#     def __str__(self):
#         return "\n".join([self._horizontal_rule(),
#                           self._empty_line(),
#                           self._message_line(),
#                           self._empty_line(),
#                           self._horizontal_rule()])

#     def _empty_line(self):
#         return f"|{' '*self.width}|"

#     def _horizontal_rule(self):
#         return f'+{'-'*self.width}+'
    
#     def _lpadding(self):
#         return ' '*(((self.width - len(self.message))//2) - 1)
    
#     def _rpadding(self):
#         if (self.width - len(self.message)) % 2 == 0:
#             return self._lpadding()
#         else:
#             return self._lpadding() + ' '
    
#     def _message_line(self):
#         return f"| {self._lpadding()}{self.message}{self._rpadding()} |"

# # Comments show expected output

# banner = Banner('To boldly go where no one has gone before.', 30)
# print(banner)
# # +--------------------------------------------+
# # |                                            |
# # | To boldly go where no one has gone before. |
# # |                                            |
# # +--------------------------------------------+

# banner = Banner('')
# print(banner)
# # +--+
# # |  |
# # |  |
# # |  |
# # +--+

##PP2 RECTANGLE
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width
    
#     @property
#     def height(self):
#         return self._height
    
#     @property
#     def area(self):
#         return self.width * self.height
    
# rect = Rectangle(4, 5)

# print(rect.width == 4)        # True
# print(rect.height == 5)       # True
# print(rect.area == 20)        # True

##PP3 RECTANGLE AND SQUARES
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def area(self):
#         return self._width * self._height

# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
    


# square = Square(5)
# print(square.area == 25)      # True

##PP4 complete the program - cats
# class Pet:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
        

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age
        
#     def __str__(self):
#         return self.__class__.__name__
    
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self._color = color

#     @property
#     def color(self):
#         return self._color
    
#     @property
#     def info(self):
#         return f'My cat {self.name} is {self.age} years old and has {self.color} fur.'

# cocoa = Cat('Cocoa', 3, 'black')
# cheddar = Cat('Cheddar', 4, 'yellow and white')

# print(cocoa.info)
# print(cheddar.info)

##PP5 ANIMALS
# class Animal:
#     def __init__(self, name, age, legs, species, status):
#         self.name = name
#         self.age = age
#         self.legs = legs
#         self.species = species
#         self.status = status

#     def introduce(self):
#         return (f"Hello, my name is {self.name} and I am "
#                 f"{self.age} years old and {self.status}.")

# class Cat(Animal):
#     def __init__(self, name, age, status):
#         super().__init__(name, age, 4, 'cat', status)

#     @property
#     def speak(self):
#         return "Meow meow!"
    
#     def introduce(self):
#         return f"{super().introduce()} {self.speak}"

# class Dog(Animal):
#     def __init__(self, name, age, status, owner):
#         super().__init__(name, age, 4, 'dog', status)
#         self.owner = owner

#     @property
#     def speak(self):
#         return "Woof! Woof!"
    
#     def introduce(self):
#         return f"{super().introduce()} {self.speak}"
    
#     def greet_owner(self):
#         return f"Hi {self.owner}! {self.speak}"

# PP6 PET SHELTER
# class Pet:
#     def __init__(self, animal, name):
#         self.animal = animal
#         self.name = name
    
#     @property
#     def info(self):
#         return f'a {self.animal} named {self.name}.'
    
# class Owner:
#     def __init__(self, name):
#         self.name = name
#         self.adoptions = []

#     def number_of_pets(self):
#         return len(self.adoptions)
    
#     def print_pets(self):
#         print(f'{self.name} has adopted the following pets:')
#         for pet in self.adoptions:
#             print(pet.info)
#         print('')
    
# class Shelter:
#     def __init__(self):
#         self.owners = []

#     def adopt(self, owner, pet):
#         owner.adoptions.append(pet)
#         if owner not in self.owners:
#             self.owners.append(owner)
        
#     def print_adoptions(self):
#         for owner in self.owners:
#             owner.print_pets()

# cocoa   = Pet('cat', 'Cocoa')
# cheddar = Pet('cat', 'Cheddar')
# darwin  = Pet('bearded dragon', 'Darwin')
# kennedy = Pet('dog', 'Kennedy')
# sweetie = Pet('parakeet', 'Sweetie Pie')
# molly   = Pet('dog', 'Molly')
# chester = Pet('fish', 'Chester')

# phanson = Owner('P Hanson')
# bholmes = Owner('B Holmes')

# shelter = Shelter()
# shelter.adopt(phanson, cocoa)
# shelter.adopt(phanson, cheddar)
# shelter.adopt(phanson, darwin)
# shelter.adopt(bholmes, kennedy)
# shelter.adopt(bholmes, sweetie)
# shelter.adopt(bholmes, molly)
# shelter.adopt(bholmes, chester)

# shelter.print_adoptions()
# print(f"{phanson.name} has {phanson.number_of_pets()} "
#       "adopted pets.")
# print(f"{bholmes.name} has {bholmes.number_of_pets()} "
#       "adopted pets.")

##PP7 Refactoring Vehicles
# class Vehicle:
#     WHEELS = None

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
        
#     def get_wheels(self):
#         return self.WHEELS

#     def info(self):
#         return f"{self.make} {self.model}"
    
# class Car(Vehicle):
#     WHEELS = 4

# class Motorcycle(Vehicle):
#     WHEELS = 2
    
# class Truck(Vehicle):
#     WHEELS = 6

#     def __init__(self, make, model, payload):
#         super().__init__(make, model)
#         self.payload = payload

##PP8 MOVING
# class WalkMixin:
#     def walk(self):
#         return f"{self.name} {self.gait()} forward"
    
# class Person(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"

# class Cat(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"

# class Cheetah(Cat):
#     def gait(self):
#         return "runs"

# class Noble(Person):
#     def __init__(self, name, title):
#         super().__init__(name)
#         self.title = title

#     def gait(self):
#         return 'struts'
    
#     def walk(self):
#         return f'{self.title} {super().walk()}'

    

# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"

# byron = Noble("Byron", "Lord")
# print(byron.walk())  # "Lord Byron struts forward"
# print(byron.name)    # "Byron"
# print(byron.title)   # "Lord"

# PP9 
# class House:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         self._price = value

#     def __lt__(self, other):
#         if isinstance(other, House):
#             return self.price < other.price
        
#     def __gt__(self, other):
#         if isinstance(other, House):
#             return self.price > other.price

# home1 = House(100000)
# home2 = House(150000)
# if home1 < home2:
#     print("Home 1 is cheaper")
# if home2 > home1:
#     print("Home 2 is more expensive")

# PP11 WALLET 1

# class Wallet:
#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         if isinstance(other, Wallet):
#             return Wallet(self.amount + other.amount)
#         return NotImplemented

#     def __str__(self):
#         return f"Wallet with ${self.amount}"
    
# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet)          # Wallet with $80.

# PP13
class Transform:
    def __init__(self, data):
        self.data = data

    def uppercase(self):
        return self.data.upper()

    @classmethod
    def lowercase(cls, str_):
        return str_.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz
    




