# PP1
# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }
# total_age = 0
# for info in munsters.values():
#     if info['gender'] == 'male':
#         total_age += info['age']

# print(total_age)

# total_age = sum([info['age'] 
#              for info in munsters.values()
#              if info['gender'] == 'male'])

# print(total_age)

# PP2
# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# new_lst = []
# for i in lst:
#     new_lst.append(sorted(i))

# print(new_lst)

# new_lst = [sorted(i) for i in lst]
# print(new_lst)

# PP3
# new_lst = [sorted(i, key=str) for i in lst]
# print(new_lst)

# PP4
# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# dict1 = {item[0] : item[1] for item in lst}
# print(dict1)

# PP5
# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# def sum_odd(sublist):
#     odd_numbers = [num for num in sublist if num % 2 != 0]
#     return sum(odd_numbers) 
                    
# sorted_list = sorted(lst, key=sum_odd)
# print(sorted_list)

# PP6
# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# new = [{key : value +1  for key, value in item.items()}
#        for item in lst]

# print(new)

# PP7
# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
# # # new_list = []

# # # for sublist in lst:
# # #     new_sublist = []
# # #     for elem in sublist:
# # #         if elem % 3 == 0:
# # #             new_sublist.append(elem)

# # #     new_list.append(new_sublist)
    
# # # print(new_list)

# # new_list = []
# # for sublist in lst:
# #     new_sublist = [num for num in sublist if num % 3 == 0]
# #     new_list.append(new_sublist)

# # print(new_list)
# new_list = [[num for num in sublist if num % 3 == 0] for sublist in lst]
# print(new_list)
# PP8
'''
input: dictionary
output: list
    return Color for fruits
    return SIZE for vegetables

algorithm
    set up an empty list
    iterate through dict1 
        if "type" is a fruit add the Color to list
            change case to Capitalize
        if type is a vegatable add SIZE to the list
            change case to UPPER
    return new_list

'''
# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }
# def transform_item(item):
#     if item['type'] == 'fruit':
#         return [color.capitalize() for color in item['colors']]
#     else:
#         return item['size'].upper()

# result = [transform_item(item) for item in dict1.values()]

# print(result)

# PP9
# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]
# new_list = []
# for subdict in lst: 
#     new_subdict = {}
#     for key, value in subdict.items():
#         for elem in value:
#             new_value = []
#             if all(elem % 2 == 0 for elem in value):
#                 new_value.append(elem)
#         new_subdict[key] = new_value
#     if all(value.isalnum() for value in subdict):
#         new_list.append(new_subdict)

# print(new_list)
# PP10

# def generate_UUID():
#     import random
#     hex_chars = "0123456789abcdef"
#     section = [8, 4, 4, 4, 12]
#     uuid = ''
#     for section in section:
#         uuid += f'{''.join(random.sample(hex_chars, section))}-'
#     return uuid[:-1]

# print(generate_UUID())
# print(generate_UUID())
# print(generate_UUID())
# print(generate_UUID())
# PP11
# dict1 = {
#     'first':  ['the', 'quick'],
#     'second': ['brown', 'fox'],
#     'third':  ['jumped'],
#     'fourth': ['over', 'the', 'lazy', 'dog'],
# }

# # list_of_vowels = []
# # for lst in dict1.values():
# #     for string in lst:
# #         for char in string:
# #             if char in 'aeiou':
# #                 list_of_vowels.append(char)

# list_of_vowels = [char for lst in dict1.values() 
#                        for string in lst 
#                        for char in string if char in 'aeiou']

    
# # Your code goes here

# print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']


