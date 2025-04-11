#PP1 COUNTDOWN

import pdb

# def decrease(counter):
#     return counter - 1

# counter = 10

# for _ in range(10):
#     print(counter)
#     counter = decrease(counter)

# print('LAUNCH!')

# PP2 Reverse String 

# def reverse_string(string):
#     string = string[::-1]

#     return string

# print(reverse_string("hello"))# == "olleh")

# PP3 MULTIPO)LY list

# def multiply_list(lst):
#     for idx in range(len(lst)):
#         lst[idx] *= 2

#     return lst

# print(multiply_list([1, 2, 3]))# == [2, 4, 6])

# PP4 Key Check

# def get_key_value(my_dict, key):
#     return my_dict.get(key)
        
# print(get_key_value({"a": 1}, "b"))

# PP5 CALENDAR EVENT CHECKER

# events = {
#     "2023-08-13": ["Python debugging exercises"],
#     "2023-08-14": ["Read 'Automate the Boring Stuff'"],
#     "2023-08-15": ["Webinar: Python for Data Science"],
# }

# def is_date_available(date):
#     if date in events:
#         return False

#     return True

# print(is_date_available("2023-08-14"))  # should return False
# print(is_date_available("2023-08-16"))  # should return True

# PP6 MUTABLE DEFAULT ARGUMENTS

# def append_to_list(value):
#     return [value]

# print(append_to_list(1))# == [1])
# print(append_to_list(2))# == [2])

# # PP7 SHADOW

# def sum_mult(numbers, factor):
#     return factor * sum(numbers)

# numbers = [1, 2, 3, 4]
# print(sum_mult(numbers, 2) == 20)

# PP8 COPY ISSUES

# import copy

# original = [[1], [2], [3]]
# copied = copy.deepcopy(original)

# original[0][0] = 99

# print(copied[0] == [1])

# PP9 Set Modifications

# data_set = {1, 2, 3, 4, 5}

# data_set = {item for item in data_set if item % 2 != 0}

# PP10 LIST DUPLICATION

# data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = []

# for num in data:
#     if num not in unique_data:
#         unique_data.append(num)



# print(unique_data == [4, 2, 1, 3]) # order not guaranteed

