# PP1 Alphabetical Numbers

# dict1 = {
#     0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
#     7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 
#     13: 'thirteen', 14: 'forteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
#     18: 'eighteen', 19: 'nineteen'   
# }

# def alphabetic_number_sort(lst):
#     alpha_list = []
#     for num in lst:
#         alpha_list.append(dict1[num])

#     alpha_list.sort()
    
#     sorted_num_list = []
#     for alnum in alpha_list:
#         for key, value in dict1.items():
#             if value == alnum:
#                 sorted_num_list.append(key)
    
#     return sorted_num_list
    
# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
#                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

# print(alphabetic_number_sort(input_list))# == expected_result)
# # Prints True

# PP2 Merge Sets
# 
# def merge_sets(l1, l2):

#     return set(l1) | set(l2)



# list1 = [3, 5, 7, 9]
# list2 = [5, 7, 11, 13]
# print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

# PP3 Immutable Intersection
# def intersection(l1, l2):
#     return frozenset(l1) & frozenset(l2)

# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 8]
# expected_result = frozenset({8})
# print(intersection(list1, list2) == expected_result) # True

# # PP4 ARRANGE A DICTIONARY
# def sort_key(item):
#     return item[1]

# def order_by_value(dict):  
#     sorted_items = sorted(dict.items(), key=sort_key)
#     return [key for key, value in sorted_items]

# my_dict = {'p': 8, 'q': 2, 'r': 6}
# keys = ['q', 'r', 'p']
# print(order_by_value(my_dict) == keys)  # True

# PP5 Unique Elements

# def unique_from_first(l1, l2):
#     return {num for num in l1 if num not in l2}

# list1 = [3, 6, 9, 12]
# list2 = [6, 12, 15, 18]
# print(unique_from_first(list1, list2) == {9, 3})

# PP6 LEADING SUBSTRINGS
# def leading_substrings(string):
#     # substring_list = []
#     # count = 1
#     # for letter in string:
#     #     substring_list.append(string[:count])
#     #     count += 1
#     # return substring_list

#     #OR

#     return [string[:idx +1] for idx in range(len(string))]
        

# # # All of these examples should print True
# # print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# # print(leading_substrings('a') == ['a'])
# # print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# # PP7 ALL ALL SUBSTRINGS

# def substrings(string):
# #     all_substrings = []
# #     for i in range(len(string)):
# #         all_substrings += (leading_substrings(string[i:]))
# #     return all_substrings
# #OR
#     return [substring for idx in range(len(string)) for substring in leading_substrings(string[idx:])]
    
# # expected_result = [
# #     "a", "ab", "abc", "abcd", "abcde",
# #     "b", "bc", "bcd", "bcde",
# #     "c", "cd", "cde",
# #     "d", "de",
# #     "e",
# # ]

# # print(substrings('abcde'))# == expected_result)  # True

# # PP8 PALINDROMATIC SUBSTRINGS

# def palindromes(string):
#    return [substring 
#             for substring in substrings(string)
#             if len(substring) > 1 and substring == substring[::-1]]


# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True

# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

# PP9 INVENTORY ITEM TRANSACTIONS
'''
INPUT a number and a list
output a list containgin a dictionary 

explicit: will be integers and a list containign a dictionary
implicit: no worries of a none return.

DS - list/dictionary comprehension 

alg
    1. create new list
    2. iterate through the list
    3. lookup the desired element in list
        if the first index of any of the list elements is the matching number
        add the data in the new list
    4. return the new list
'''

# def transactions_for(ID, list):
    
#     return [dict for dict in list if dict['id'] == ID]

# # transactions = [
# #     {"id": 101, "movement": 'in',  "quantity":  5},
# #     {"id": 105, "movement": 'in',  "quantity": 10},
# #     {"id": 102, "movement": 'out', "quantity": 17},
# #     {"id": 101, "movement": 'in',  "quantity": 12},
# #     {"id": 103, "movement": 'out', "quantity": 20},
# #     {"id": 102, "movement": 'out', "quantity": 15},
# #     {"id": 105, "movement": 'in',  "quantity": 25},
# #     {"id": 101, "movement": 'out', "quantity": 18},
# #     {"id": 102, "movement": 'in',  "quantity": 22},
# #     {"id": 103, "movement": 'out', "quantity": 15},
# # ]

# # print(transactions_for(101, transactions) ==
# #       [
# #           {"id": 101, "movement": "in",  "quantity":  5},
# #           {"id": 101, "movement": "in",  "quantity": 12},
# #           {"id": 101, "movement": "out", "quantity": 18},
#     #   ]) # True
# # PP10 INVENTORY ITEM AVAILABILITY

# def is_item_available(ID, lst):
#     transactions = transactions_for(ID, lst)
#     tracker = 0

#     for item in transactions:
#         if item['movement'] == 'in':
#             tracker += item['quantity']
#         else:
#             tracker -= item['quantity']

#     return tracker > 0
    
    
# transactions = [
#     {"id": 101, "movement": 'in',  "quantity":  5},
#     {"id": 105, "movement": 'in',  "quantity": 10},
#     {"id": 102, "movement": 'out', "quantity": 17},
#     {"id": 101, "movement": 'in',  "quantity": 12},
#     {"id": 103, "movement": 'out', "quantity": 20},
#     {"id": 102, "movement": 'out', "quantity": 15},
#     {"id": 105, "movement": 'in',  "quantity": 25},
#     {"id": 101, "movement": 'out', "quantity": 18},
#     {"id": 102, "movement": 'in',  "quantity": 22},
#     {"id": 103, "movement": 'out', "quantity": 15},
# ]

# print(is_item_available(101, transactions) == False)  # True
# print(is_item_available(103, transactions) == False)  # True
# print(is_item_available(105, transactions) == True)   # True