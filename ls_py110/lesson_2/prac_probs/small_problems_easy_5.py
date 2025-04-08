# PP1 INVERTING DICTIONAR

# def invert_dict(dictionary):
#     return {value: key for key, value in dictionary.items()}

# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }) == {
#           'fruit': 'apple',
#           'vegetable': 'broccoli',
#           'fish': 'salmon',
#       })  # True

# PP2 RETAIN sPECIFIC kEYS

# def keep_keys(dict, lst_keys):
#     new_dictionary = {key: value for key, value in dict.items() if key in lst_keys}
#     return new_dictionary


# input_dict = {
#     'red': 1,
#     'green': 2,
#     'blue': 3,
#     'yellow': 4,
# }

# keys = ['red', 'blue']
# expected_dict = {'red': 1, 'blue': 3}
# print(keep_keys(input_dict, keys) == expected_dict) # True

# PP3 DELETE VOWELS

# def remove_vowels(lst):

#     new_list = []    
    
#     for string in lst:
#         new_string = ''
#         for char in string:
#             if char not in 'aeiouAEIOU':
#                 new_string += char
#         new_list.append(new_string)
        
    
#     return new_list

#   # All of these examples should print True
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True

# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True

# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True

# PP4 HOW3 LONG ARE YOU

# def word_lengths(words=[]):
#     word_list = []

#     if len(words) > 0:
#         split_words = words.split(' ')
#         for word in split_words:
#             word_list.append(f'{word} {str(len(word))}')

#     return word_list
# # All of these examples should print True
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True

# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                    'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True

# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                    'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True

# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True

# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

# PP5 LIST ELEMENT MULTIPLICATION
# def multiply_items(l1, l2):
    # l3 = []
    # count = 0
    # for num in l1:
    #     l3.append(num * l2[count])
    #     count += 1
    # return l3

# OR

    # return [l1[idx] * l2[idx] for idx in range(len(l1))]
    
# OR

    # return [num1 * num2 for num1, num2 in zip(l1, l2)]

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# PP6 SUM OF SUMS

# def sum_of_sums(ls):
#     new = 0
#     for idx in range(len(ls)):
#         new += sum(ls[:len(ls) - idx])
#     return new

#OR

    # return [sum(sum(ls[:len(ls) - idx]) for idx in range(len(ls)))][0]

#SUGESSTED

#     total_sum = 0
#     running_sum = 0
#     for num in ls:
#         running_sum += num
#         total_sum += running_sum
    
#     return total_sum

# print(sum_of_sums([3, 5, 2]) == 21)               # True
# # (3) + (3 + 5) + (3 + 5 + 2) --> 21

# print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

# print(sum_of_sums([4]) == 4)                      # True

# PP7 SUM OF DIGITS
# def sum_digits(number):
#     # list_ints = []

#     # for i in list(str(number)):
#     #     list_ints.append(int(i))
#     # return sum(list_ints)
# # OR
#     return sum([int(i) for i in str(number)])

# print(sum_digits(23) == 5)              # True
# print(sum_digits(496) == 19)            # True
# print(sum_digits(123456789) == 45)      # True

# PP8 STAGGERED CASE p1
# def staggered_case(string):
# #     new_string = ''
# #     for idx, char in enumerate(string):
# #         if idx % 2 == 0:
# #             new_string += char.upper()
# #         else:
# #             new_string += char.lower()
# #     return new_string

# # #OR 

#     return ''.join([char.upper() if idx % 2 == 0 
#                     else char.lower() for idx, char in enumerate(string)])

# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

# PP9 STAGGERED CASE p2
# def staggered_case(string):
#     new_string = ''
#     count = 0

#     for char in string:
#         if char.isalpha():
#             if count % 2 == 0:
#                 new_string += char.upper()
#                 count += 1
#             else:
#                 new_string += char.lower()
#                 count += 1
#         else:
#             new_string += char

#     return new_string


# string = 'I Love Launch School!'
# result = "I lOvE lAuNcH sChOoL!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_cApS"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

# PP10 REMOVE CONSECUTIVE DUPLICATES



# def unique_sequence(numbers):
#     return [value
#             for idx, value in enumerate(numbers)
#             if idx == 0 or value != numbers[idx-1]]       


# original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4, 3]
# expected = [1, 2, 6, 5, 3, 4, 3]
# print(unique_sequence(original) == expected)      # True