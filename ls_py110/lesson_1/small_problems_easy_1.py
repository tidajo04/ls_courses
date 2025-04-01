# P1 Searchin 101
# '''
# input: a series of user inputs
# output: interpolated phrase with the statment of whether the last input is in the grooup of prior inputs

# explicit: must solicit a prompt answer. 
# implicit: all answers will be numbers (for comparison, integer or string, shouldnt matter)

# data structure: strings with user input, filling an empty list.

# algorithm.
# 1. ask the user toi input a number
# 2. create an empty list
# 3. append the list with the user inputs
# 4. compare the last input with the filled list to check if the last is in the list.
# 5. return a statement interpolation 
#     - convert the list into a string o fnumbers separated only by commas (no spaces)
# '''

# request_number = ['1st', '2nd', '3rd', '4th', '5th', 'last']
# num_list = []

# for req in request_number:
#     num_list.append(input(f'Enter the {req} number:'))

# if num_list[-1] in num_list[:5]:
#     print(f'{num_list[-1]} is in {','.join(num_list[:5])}')
# else:
#     print(f'{num_list[-1]} isn\'t in {','.join(num_list[:5])}')

#PP2 Palindromatic Strings(part 1)
'''
input: a string
output: Boolean - is string palandrome? T/F

explicit: -function returns boolean
        -eval is case sensitive
        -any character matters (whitespace, puctuation etc.)
implicit: strings may be phrases and numbers and may have other characters

data structures: may need to use List and string functions. .reverse() list method as a check.

Algorithm:
-convert the string into a list of all characters as an element
-use the reverse method to check if same 
'''

# def is_palindrome(string):
#     return string == string[::-1]

# ## PP3 palindromic strings (part2)
# def is_real_palindrome(string):
#     cleaned_string = ''
#     for char in string:
#         if char.isalnum():
#             cleaned_string += char.casefold()
#     return is_palindrome(cleaned_string)

# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

#PP4 RUNNING TOTALS
'''
input: list of numbers
output: new list (each element is the running total of the original list)

explicit:
    - all inputs will be int or blank
    -if blank list return a new blank list
implicit:
    - negative numbers not an issue

data structures: all can be done through lists

Algorithm:
    - create a new empty list
    -iterate through original list and add the sum of each iteration to the new list
        -each addition to the new list should add the previous number to itself before being put into new list
    -return new list

'''
# def running_total(lst_numbers):
#     totals_list = []
    
#     for i in range(len(lst_numbers)):
#         totals_list.append(lst_numbers[i] + sum(lst_numbers[:i]))
#     return totals_list
            

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# PP5 LETTER COUNTER P1
'''
input: string
output: dictionary (showing number of words by size/length)

explicit: 
    words consist of any non-space characters
    adjacent punctuation is included in word size
    an empty string must return an empty dicitonary
implicit: 
    n/a

datastructures. converting strings to a list of "words" will make dictionary population possible. 

algorithm:
    create an empty dictionary 
    split the list into its words
    iterate through the list to get a count of characters in each word
    populate the dictionary using the number of letters as the key and the frequency as the value

'''
# def word_sizes(string):
#     length_freq_dict = {}
#     split_string = string.split(' ')
#     if string == '':
#         return {}
#     else:
#         for s in split_string:
#             count = 0
#             count += len(s)
#             if length_freq_dict.get(count) == None:
#                 length_freq_dict[count] = 1
#             else:
#                 length_freq_dict[count] += 1
#         return length_freq_dict

# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})

#PP6 LETTER COUNTER p2
# def cleaned_string(s):
#     cleaned_string = ''
#     for char in s:
#         if char.isalpha():
#             cleaned_string += char

#     return cleaned_string

# def word_sizes(string):
#     length_freq_dict = {}
#     split_string = string.split(' ')

#     if string == '':
#         return {}
#     else:
#         for s in split_string:
#             s = cleaned_string(s)
#             count = 0
#             count += len(s)
#             if length_freq_dict.get(count) == None:
#                 length_freq_dict[count] = 1
#             else:
#                 length_freq_dict[count] += 1
#         return length_freq_dict
    
# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

# PP7 LETTER SWAP
'''
input: a string of words separated by whitespace
output: a string of the same words with the 1st and last letters of each word swapped

explicit: 
    every word is at least 1 letter
    no blank strings
    no leading or trailing whitespace
    no need to account for punctuation

datastructure 
    can handle using string concatination makeing a new string referenceing the indexes
    will need to split into a list of words to habdle each separately


algorithm:
    split string into a list of substrings
    iterate through each substring to revese the first and last index
        initiate a blank string 
        if 1 character, make no change
        if 2 characters, use reverse
        if 3 or more, concatinate last + mid+ first
    join the list with space separator and initiate a new return string.
'''
# def swap(string):
#     listed_string = string.split(' ')
#     altered_list = []
#     for s in listed_string:
#         if len(s) == 1:
#             altered_list.append(s)
#         else:
#             altered_list.append(s[-1] + s[1:- 1] + s[0])
    
#     return ' '.join(altered_list)


# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

# PP8 CONVERT A STRING TO NUMBER
'''
input: a string of numeric characters
output: an integer 

explicit:
    cannot use the int() method
    no need to worry on pos/neg

data structure: 
    could create a simple dictionary associateing int value to string value
    knowing the length of the string, can iterate through with mutiples of 10 to 
    calculate the integer
algorithm:
    creat a dictionary of all numbers with an integer, string key value
    create function
        create "integer" variable, set to 0. 
        using the dictionary to get the associated integer, multiply the first index by 10**length
        add the result to "integer"
        remove the first index
        repeat
        
'''
# numbers_dict = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 0:"0"}

# def string_to_integer(num_string):
#     numbers_dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}    
#     integer = 0
#     count = 1
#     for num in num_string:
#         integer += numbers_dict[num] * 10**(len(num_string) - count)
#         count += 1
#     return integer

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

#PP9 CONVERT STRING TO A SIGNED NUMBER
# def cleaned_sign(string):
#     cleaned_string = ''
#     for i in string:
#         if i.isnum():
#             cleaned_string += i
#     return cleaned_string

# def string_to_signed_integer(num_string):
#     numbers_dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}    
#     integer = 0
#     count = 1
#     for num in num_string:
#         if num == '-' or num == '+':
#             count += 1
#             continue
#         else:
#             if num_string[0] == '-':    
#                 integer -= numbers_dict[num] * 10**(len(num_string) - count)
#                 count += 1
#             else:
#                 integer += numbers_dict[num] * 10**(len(num_string) - count)
#                 count += 1
#     return integer

# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True

#PP10 CONVERT A NUMBER TO A STRING


# def integer_to_string(number):
#     numbers_dict = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 0:"0"}
#     string = ''
#     if number == 0:
#         return '0'
#     else:
#         while number > 0:
#             string += numbers_dict[number % 10]
#             number //= 10
#         return string[::-1]

# # print(integer_to_string(4321) == "4321")              # True
# # print(integer_to_string(0) == "0")                    # True
# # print(integer_to_string(5000) == "5000")              # True
# # print(integer_to_string(1234567890) == "1234567890")  # True

# #PP10 CONVERT A signed NUMBER TO A STRING


# def signed_integer_to_string(number):
#     if number < 0:
#         return f'-{integer_to_string(-number)}'
#     elif number > 0:
#         return f'+{integer_to_string(number)}'
#     else:
#         return '0'
        

# print(signed_integer_to_string(4321) == "+4321")  # True
# print(signed_integer_to_string(-123) == "-123")   # True
# print(signed_integer_to_string(0) == "0")         # True