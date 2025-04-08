# PP1
# lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

# print(lst1[2][1][3])
# lst2 = [
#     {
#         'first': ['a', 'b', 'c'],
#         'second': ['d', 'e', 'f']
#     },
#     {
#         'third': ['g', 'h', 'i']
#     }
# ]
# print(lst2[1]['third'][0])
# lst3 = [['abc'], ['def'], {'third': ['ghi']}]
# print(lst3[2]['third'][0][0])
# dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
# print(dict1['b'][1])
# # This one is much more challenging than it looks! Try it, but don't
# # stress about it. If you don't solve it in 10 minutes, you can look
# # at the answer.
# dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
# print(list(dict2['3rd'].keys())[0])

# # PP2
# lst1 = [1, [2, 3], 4]
# lst1[1][1] = 4

# lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
# lst2[2] = 4

# dict1 = {'first': [1, 2, [3]]}
# dict1['first'][2][0] = 4

# dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
# dict2['a']['a'][2] = 4

# # PP4
# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }
# for name, info in munsters.items():
#     print(f'{name} is a {info['age']}-year-old {info['gender']}.')