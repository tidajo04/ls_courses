##PP 1 Generic Greeting
# class Cat:

#     @classmethod
#     def generic_greeting(cls):
#         print('Hello, I\'m a cat!')

# kitty = Cat()
# Cat.generic_greeting()
# type(kitty).generic_greeting()

##PP2 Hello Chloe!

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, value):
#         self._name = value

#     def rename(self, new_name):
#         self.name = new_name


# kitty = Cat('Sophie')
# print(kitty.name)             # Sophie
# kitty.rename('Chloe')
# print(kitty.name)             # Chloe

##PP3 ID yourself p1
# class Cat:
#     def __init__(self, name):
#         self._name = name
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, value):
#         self._name = value

#     def identify(self):
#         return self

# kitty = Cat('Sophie')
# print(kitty.identify())  

##PP4
# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
#     def personal_greeting(self):
#         print(f'Hello! My name is {self.name}!')
    
# kitty = Cat('Sophie')
# kitty.personal_greeting()

##PP5 Counting Cats
# class Cat:
#     cat_count = 0

#     def __init__(self):
#         Cat.cat_count += 1

#     @classmethod
#     def total(cls):
#         print(cls.cat_count)

# Cat.total()         # 0

# kitty1 = Cat()
# Cat.total()         # 1

# kitty2 = Cat()
# Cat.total()         # 2

# print(Cat())        # <__main__.Cat object at 0x104ed7290>
# Cat.total()         # 3

##PP6
# class Cat:
#     COLOR = 'purple'

#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def greet(self):
#         print(f"Hello! My name is {self.name} and I'm a {Cat.COLOR} cat!")

# kitty = Cat('Sophie')
# kitty.greet()
# Hello! My name is Sophie and I'm a purple cat!

##PP7
# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
#     def __str__(self):
#         return f'I\'m {self.name}!'

# # Comments show expected output
# kitty = Cat('Sophie')
# print(kitty)        # I'm Sophie!