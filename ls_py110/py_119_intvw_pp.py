# pp1
'''
input: list of numbers
output: list of numbers
    representing each unique number's value of occurences of other numbers smaller than it in the prime list

explicit, 
    if no numbers smaller, return 0.
    in counting the number of smaller numbers, only count each occurance once even if multiple
implicit, no need to account for an empty list input or non-integers

dataStructure:
    list comprehension to iterate through should work. the trick is to set conditional 
    statements to filter out repeated numbers and lesser than numbers

algorithm. 
    1. create function`smaller_numbers_than_current(lst)`
    2. set 'result' as the value for the list comprehension.
    3. iterate through input list
        initialize a count variable = 0
        nest another iteration to look through each value in the set of the list that updates the count
          if the value is less than the current number
        return count  
        reset count
    return result
'''

# def smaller_numbers_than_current(lst):
#     result = []
#     unique_num = set(lst)
#     for current_num in lst:
#         count = 0
#         for unique_num in unique_num:
#             if unique_num < current_num:
#                 count += 1
#         result.append(count)
#     return result
        
# print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
# print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
# print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
# print(smaller_numbers_than_current([1]) == [0])

# my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
# result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
# print(smaller_numbers_than_current(my_list) == result)

# PP2
'''
input: list of integers
output: the minumum sum of 5 consequtive numbers in the list

explicit: 
    if less than 5 integers in the input list, return None
    consecutive list slices
    negatrive numbers are possible
implicit: no need to worry about empty lists as any other than 5+ returns None

data structures:
    sequence slicing and iterating through a range based on the length of the sequence

algorthm. 
    define ffunctoin 'minimum_sum(lst)'
    1. set a break condition 
        if length of list is < 5, return None
    2. using a while loop that terminates when the end of the slice is greater than the length of the list
        1. make an empty list to hold slices
            starting at index 0, return the sum of list[idx:idx+5]
            append the result to the list (or use list comprehension)
        2. return the minimum of that list
'''

# def minimum_sum(lst):
#     if len(lst) < 5:
#         return None
    
#     return min([sum(lst[idx:idx+5]) for idx in range(len(lst) - 4)])

# print(minimum_sum([1, 2, 3, 4]) is None)
# print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
# print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
# print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
# print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

# pp3
'''
input: string 
output: new string with every second character of every 3rd word converted to uppercase. 

explicit: if third word is 1 characdter, no change
implicit: no consideration for puntuation needed,
         and a 'word' is any grouping of alpha chjars separated by space
         no consideration for empty strings

data structure: 
    shoul;d be able to use a list comprehesion and re 'join' the list to make the new string

alg. 
    1. define function named to_wierd_case
    2. initialize 'wierd_string' to a joined list comprehension
        a. can easily iterate through checking for 3rd word by using idex value+1 % 3 = 0
        b. for each word, if the word is a target word, iterate through word and change every second character
        * may benefit from starting with for loops and transforming into a comprehension to make sure i understand. 
    3. return wierd_string
'''

# def to_weird_case(string):
#     string_list = string.split()
#     weird_string = []
#     for idx in range(len(string_list)):
#         if (idx + 1) % 3 == 0:
#             wierd_word = ''
#             for sub_idx in range(len(string_list[idx])):
#                 if sub_idx % 2 != 0:
#                     wierd_word += string_list[idx][sub_idx].upper()
#                 else:
#                     wierd_word += string_list[idx][sub_idx]
#             weird_string.append(wierd_word)
#         else:
#             weird_string.append(string_list[idx])
#     return ' '.join(weird_string)

# original = 'Lorem Ipsum is simply dummy text of the printing world'
# expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
# print(to_weird_case(original) == expected)

# original = 'It is a long established fact that a reader will be distracted'
# expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
# print(to_weird_case(original) == expected)

# print(to_weird_case('aaA bB c') == 'aaA bB c')

# original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
# expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
# print(to_weird_case(original) == expected)

# pp4
'''
input list of integers
output: tuple of the two closest integers

explicit: all integers,
implicit: all positive, no empty list or list of 1 to be controlled for

data structure: progressive iteration and comparison through the list will acount for all cases. 

alg. 
 1. initialize a variable called result = ()
 2. initialize variable called tup_dif set equal to the difference of the result. 
 2. iterate through the list of integers, comparing each current number with all others subsequent to it
    a. for the first comparison, add the tupple to result.
    b. for each subsequent tuple, calculate the difference and test against the tup_dif.
    c. if the tup dif of the current tuple is less, update the result 
 3. return result.
# '''
# def tup_diff(tup):
#         return abs(tup[0] - tup[1]) 

# def closest_numbers(int_list):
#     result = (int_list[0], int_list[1])
#     result_diff = tup_diff(result)

#     for idx in range(len(int_list) - 1):
#         for idx2 in range(idx + 1, len(int_list)):
#             current_pair = (int_list[idx], int_list[idx2])
#             current_diff = tup_diff(current_pair)
#             if current_diff < result_diff:
#                  result = current_pair
#                  result_diff = current_diff
                 
#     return result

# def closest_numbers(lst):
#     tuple_list = [(lst[i], lst[j]) for i in range(len(lst) - 1) for j in range(i + 1, len(lst))]
    
#     result = min(tuple_list, key=lambda tup: abs(tup[0] - tup[1]))
#     return result       
            
# print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# products = [
#     {"name": "Laptop", "price": 899.99, "category": "Electronics"},
#     {"name": "Shoes", "price": 59.99, "category": "Apparel"},
#     {"name": "Smartphone", "price": 499.99, "category": "Electronics"},
#     {"name": "T-Shirt", "price": 19.99, "category": "Apparel"},
#     {"name": "Headphones", "price": 129.99, "category": "Electronics"},
#     {"name": "Jacket", "price": 89.99, "category": "Apparel"},
#     {"name": "Smartwatch", "price": 199.99, "category": "Electronics"}
# ]

# result = sorted(products, key=lambda x: x['price'])
# print(result)

# pp5
'''
input: string (can have nonalpha and diff cases)
output: string, single character that most frequent in input string (if tied, first occurance)

explicxit: case doesnt matter (use casefold), always return the lower.
implict: no worries about empty strings 

DS: could split into a list then sort by count and index position

alg. 
    1. split string into list of lowercase characters in string
    2. use sorted to re-order the list by each characters frewuency in the list, then by its index position in the original string. 
    3. return index [0] of this list
'''

# def most_common_char(my_str):
#     lower_list = list(my_str.casefold())
#     return sorted(lower_list, key=lambda char: lower_list.count(char), reverse=True)[0]

# print(most_common_char('Hello World') == 'l')
# print(most_common_char('Mississippi') == 'i')
# print(most_common_char('Happy birthday!') == 'h')
# print(most_common_char('aaaaaAAAA') == 'a')

# my_str = 'Peter Piper picked a peck of pickled peppers.'
# print(most_common_char(my_str) == 'p')

# my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
# print(most_common_char(my_str) == 'e')

# pp6
'''
input: string arguyment
output: dictionary (key = lowercase letters in the string, value = frequency)

explicit: skip over/ignore nonalpha characters and uppercase
            if no lowercase exist, return an empty dict.

implicti: no need to account for no argument input, will always be a string.

ds: use dicitonary comnprehension and return the dicitonary

alg. 
    1. iterate through the string
    2. check if alpha and lowercase
    3.  if yes, add to dicionary
        use .setdefault to create the value 0 then add to it.

'''
# def count_letters(my_str):
#     lower_frequency = {}
#     for char in my_str:
#         if char.isalpha() and char.islower():
#             lower_frequency[char] = lower_frequency.get(char, 0) + 1
#     return lower_frequency
  

# expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
# print(count_letters('woebegone') == expected)

# expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
#             'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
# print(count_letters('lowercase/uppercase') == expected)

# expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
# print(count_letters('W. E. B. Du Bois') == expected)

# print(count_letters('x') == {'x': 1})
# print(count_letters('') == {})
# print(count_letters('!!!') == {})

# pp7

'''
input: list of integers
output: number of identical pairs

exp: if list is empty or contains one value, return 0 (also if there are no pairs)
    if a number occurs more than twice, treat it as a new pair (1,1,1,1 =2; 1,1,1,1,1 = 2; 1,1,1,1,1,1 = 3)

d.s. could use .count to shortcut this mathmatically. iterate through each value  with .count then add up the floor division of each return value top get the number of pairs.
 algorithm: 
 1. set up empty condition as = 0
 2. set count = 0
 2. iterate through a set of the list
    a. get count of set value within the list
    b. use floor division to increment the count
3. return the count
'''
# def pairs(lst):
#     pair_count = 0
#     for num in set(lst):
#         pair_count += lst.count(num) // 2
#     return pair_count

# print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
# print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
# print(pairs([]) == 0)
# print(pairs([23]) == 0)
# print(pairs([997, 997]) == 1)
# print(pairs([32, 32, 32]) == 1)
# print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

# pp8