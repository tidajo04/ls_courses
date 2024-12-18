# ex 1
# def first(list):
#     return None if len(list) == 0 else list[0]

# print(first(['Earth', 'Moon', 'Mars']))
# print(first([]))  # Earth

# ex2
# def last(list):
#     return None if len(list) == 0 else list[- 1]

# print(last(['Earth', 'Moon', 'Mars']))
# print(last([]))  # Earth
# ex 3
# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
# def list_replace(list, old, new):
#     list.remove(old)
#     list.append(new)
#     return list

# list_replace(energy, 'fossil', 'geothermal')

# print(energy)
# ex 4
# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# def list_maker(string):
#     list = []
#     for char in string:
#         list.append(char)
#     return list

# print(list_maker(alphabet))

# # #alt
# # print(list(alphabet))
# ex 5
# scores = [96, 47, 113, 89, 100, 102]

# count = 0

# for score in scores:
#     if score >= 100:
#         count += 1

# print(count)

# ex 6
# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# for syn in vocabulary:
#     for word in syn:
#         print(word)

# print(new_list)
# ex 7 - true
# ex 8
# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'
# print(type(some_value1))
# print(type(some_value2))
# # alt
# print(isinstance(some_value1, list))
# print(isinstance(some_value2, list))
# ex 9
# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']
# def contains(list, word):
#     return list.count(word) > 0

# print(contains(destinations, 'Prague'))
# ex 10
# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# # print('-'.join(passcode))

# # alt
# string = ''

# for i in range(len(passcode)): #detects the number of items in the list to set a counter (each number in range of number)
#     if i > 0:
#         string += '-'
#     string += passcode[i]  

# print(string)  
# ex 11
# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']


# while grocery_list:
#     print(grocery_list[0])
#     grocery_list.remove(grocery_list[0])

# print(grocery_list)