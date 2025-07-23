## PP 1 Find the class
# print(type('hello'))
## PP 2-9 create the class
# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

#     def greet(self):
#         print(f'hello, {self.name}')

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
        


# kitty = Cat('Sophie')
# kitty.greet()
# kitty.name = 'Luna'
# kitty.greet()
##PP10 Default Person

# class Person:
    
#     def __init__(self, name='John Doe'):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
# person1 = Person()
# person2 = Person("Pepe Le Pew")

# # Comments show expected output
# print(person1.name)    # John Doe
# print(person2.name)    # Pepe Le Pew
