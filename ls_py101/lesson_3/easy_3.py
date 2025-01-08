# question1
# numbers = [1, 2, 3, 4, 6] 
# numbers.clear()
# print(numbers)
# question2
# [1, 2, 3, 4, 5]
# question3
# hello world
# question4
#have to remember that when a copy is made (not a deepcopy, which is different)
#only the outmost items are actually copied. a
#any nested items which are merely pointed to are only also now pointed to, 
#thus when the shallow copy is made with .copy() since the copy and the original 
# both point to the SAME object, if EITHER changes the object, both are updated
# question 5
# def is_color_valid(color):
#     return color == "blue" or color == "green"
#or
# def is_color_valid(color):
#     return color in ["blue", "green"] 
# print(is_color_valid('blue'))
# print(is_color_valid('pink'))
