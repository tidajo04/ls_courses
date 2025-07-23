# class InvoiceEntry:
#     def __init__(self, product_name, number_purchased):
#         self._product_name = product_name
#         self._quantity = number_purchased

#     @property
#     def quantity(self):
#         return self._quantity
    
#     @quantity.setter
#     def quantity(self, quantity):
#         self._quantity = quantity

# entry = InvoiceEntry('Marbles', 5000)
# print(entry.quantity)         # 5000

# entry.quantity = 10_000
# print(entry.quantity)         # 10_000

# class Animal:
#     def __init__(self):
#         pass

#     def speak(self, string):
#         print(string)

# class Cat(Animal):
    
#     def meow(self):
#         return self.speak("Meow")
    
# class Dog(Animal):

#     def bark(self):
#         return self.speak("woof woof")

# class KrispyKreme:
#     def __init__(self, filling, glazing):
#         self.filling = filling
#         self.glazing = glazing
    
#     def __str__(self):
#         if self.filling:
#             filling = self.filling
#         else: 
#             filling = 'Plain'
#         if self.glazing:
#             glazing = f'with {self.glazing}'
#         else:
#             glazing = ''
#         return f'{filling} {glazing}'
    
# donut1 = KrispyKreme(None, None)
# donut2 = KrispyKreme('Vanilla', None)
# donut3 = KrispyKreme(None, 'sugar')
# donut4 = KrispyKreme(None, 'chocolate sprinkles')
# donut5 = KrispyKreme('Custard', 'icing')

# print(donut1)       # Plain
# print(donut2)       # Vanilla
# print(donut3)       # Plain with sugar
# print(donut4)       # Plain with chocolate sprinkles
# print(donut5)       # Custard with icing

class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def light_status(self):
        return (f'I have a brightness level of {self.brightness} '
                f'and a color of {self.color}')

my_light = Light(50, 'Red')
print(my_light.light_status())