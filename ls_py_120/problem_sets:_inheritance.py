# class Pet:
#     def speak(self):
#         pass

#     def sleep(self):
#         return 'sleeping...'
    
#     def run(self):
#         return 'running!'

#     def jump(self):
#         return 'jumping!'
    
# class Cat(Pet):
#     def speak(self):
#         return 'meow!'

# class Dog(Pet):
#     def speak(self):
#         return 'bark!'

#     def fetch(self):
#         return 'fetching!'
    
# class Bulldog(Dog):
#     def sleep(self):
#         return 'snoring...'
    
# teddy = Dog()
# print(teddy.speak())
# print(teddy.sleep())   

# karl = Bulldog()
# print(karl.speak())       # bark!
# print(karl.sleep())        # snoring!

# pet = Pet()
# dave = Dog()
# bud = Bulldog()
# kitty = Cat()

# print(pet.run())              # running!
# print(kitty.run())            # running!
# print(kitty.speak())          # meow!
# try:
#     kitty.fetch()
# except Exception as exception:
#     print(exception.__class__.__name__, exception, "\n")
#     # AttributeError 'Cat' object has no attribute 'fetch'

# print(dave.speak())           # bark!

# print(bud.run())              # running!
# print(bud.sleep())             # "snoring!"