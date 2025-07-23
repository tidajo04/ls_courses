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
'''
input: nonempty string
output: integer of the ongest substring of consecutive integers

explicit: no empty string case, no nonalpha lowercase characters

DS: could possibly use regex... for now, better to just iterate and count

alg. 
1. initialize vowel_substring_max variable to 0
2. initialize constant VOWELS to 'aeiou'
2. iterate through string
    a. initialize variable count to 0
    3. if character is in VOWELS add to count,
         c.   if count is greater than max, update max
    d. if character is consonant reset count to 0
4. return max 
'''

# def longest_vowel_substring(string):
#     VOWELS = 'aeiou'
#     vowel_sub_max = 0
#     count = 0
#     for char in string:
#         if char in VOWELS:
#             count += 1
#             if count > vowel_sub_max:
#                 vowel_sub_max = count
#         else:
#             count = 0
#     return vowel_sub_max

# print(longest_vowel_substring('cwm') == 0)
# print(longest_vowel_substring('many') == 1)
# print(longest_vowel_substring('launchschoolstudents') == 2)
# print(longest_vowel_substring('eau') == 3)
# print(longest_vowel_substring('beauteous') == 3)
# print(longest_vowel_substring('sequoia') == 4)
# print(longest_vowel_substring('miaoued') == 5)

# PP9
'''
input: two strings
output: integer, representing the number of times the second argument occers within the first

explicit: no overlapping (i.e. no part of the second substring should be counted twice)
            second argument is never empty, and if the 1st arg is empty rhew result is alway 0

DS: iterate through string, increasing count on occurances.

alg. could use regex. 
alternative
alg:
    1. initialize count to 0
    2. initialize current slice = string
    2. check if 2nd arg in string
        if not, return count
        if yes, increment count and remove 2nd arg from string, setting as the new current string
            repeat.
'''
# def count_substrings(string, substring):
#     count = 0
#     current_slice = string
#     while True:
#         if substring not in current_slice:
#             break
#         else:
#             count += 1
#             current_slice = current_slice.replace(substring, '', 1)
#     return count

# import re

# def count_substrings(s, sub):
#     return len(re.findall(sub, s))

# print(count_substrings('babab', 'bab') == 1)
# print(count_substrings('babab', 'ba') == 2)
# print(count_substrings('babab', 'b') == 3)
# print(count_substrings('babab', 'x') == 0)
# print(count_substrings('babab', 'x') == 0)
# print(count_substrings('', 'x') == 0)
# print(count_substrings('bbbaabbbbaab', 'baab') == 2)
# print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
# print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

# pp10
'''
input: string of digits
output: an integer representing the number of even-numbered substrings thatc an be formed.

explicit: no need to acount for empty or non digit characters.

DS. how to test all possible slices... (if ending in 02468)

alg. 
1. initialize count at 0
2. if i go backwards i can just count the number of digits preceding any even digit and add to count...
    1. so stratrgin from right ot left, if a digit is even, add to count the length of the substring
    then go to next digit repeat
'''
# def even_substrings(digits):
#     count = 0
#     even_digits = '02468'
#     for idx in range(len(digits)):
#         if ''.join(reversed(digits))[idx] in even_digits:
#             count += len(''.join(reversed(digits))[idx:])
#     return count

# print(even_substrings('1432') == 6)
# print(even_substrings('3145926') == 16)
# print(even_substrings('2718281') == 16)
# print(even_substrings('13579') == 0)
# print(even_substrings('143232') == 12)

# pp11
'''
input: none,mpty string
output: tuple (string, int)

expl: al lowercase alpha chars, nonempty

DS: checking the count of a slice in the string

alg. 
1. initialize max = o
2. initialize longest_substring_repeat = string
3. test the count of largest substring in string
    a. if count is greater than the max, update max to count.
    b. update longest_substring_repeat to current substring
4. remove the last char of the substring, test again.
    
'''
# def repeated_substring(text):
#     max_repeat = 0
#     longest_sub_repeat = text
#     for i in range(len(text)):
#         candidate = text[:len(text) - i]
#         count = text.count(candidate)
#         if count > max_repeat:
#             max_repeat = count
#             longest_sub_repeat = candidate

#     return (longest_sub_repeat, max_repeat)

# print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
# print(repeated_substring('xyxy') == ('xy', 2))
# print(repeated_substring('xyz') == ('xyz', 1))
# print(repeated_substring('aaaaaaaa') == ('a', 8))
# print(repeated_substring('superduper') == ('superduper', 1))

# pp12
'''
inputL string 
out: True, if pangram, False if not

explicit: pangram is when every letter in the alphabet is used at least once
    case is irrelevent

DS: coulf iterate through alpha valriable and if each char returns true, return True, if any return false return false.

alg.
1. initialize ALPHA 'abcdefghijklmnopqrstuvwxyz'
2. iterate through ALPHA and check if each character is in the string.casefold(). 
3. if any are not, then string is not pangram
'''

# def is_pangram(string):
#     ALPHA = 'abcdefghijklmnopqrstuvwxyz'
#     for char in ALPHA: 
#         if char not in string.casefold():
#             return False
        
#     return True

# print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
# print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
# print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

# my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
# print(is_pangram(my_str) == True)

# pp13
'''
input: two string args
output: Bool True if 1st string can be rearagned to make the second

explicit, not case sensitive, no empty consideration
implicit: no repeat use

DS: simple, can just check if the lsit of arg1 is a superset of listarg2

alg. return arg1 is superset of arg 2
'''

# def unscramble(s1, s2):
    
#     for i in s2:
#         if i not in s1:
#             return False
#         else:
#             s1 = s1.replace(i, '', 1)

#     return True

# print(unscramble('ansucchlohlo', 'launchschool') == True)
# print(unscramble('phyarunstole', 'pythonrules') == True)
# print(unscramble('phyarunstola', 'pythonrules') == False)
# print(unscramble('boldface', 'coal') == True)
# print(unscramble('olc', 'cool') == False)

# pp14
'''
input: integer
output: intger, representing the SUM of all multiples of 7 or 11 that are less than the argument.

explicit: if a number is a multiple of 7 and 11, count it only once (i.e. 77 only counted once.)
        : if arg is negative return 0

DS MAth, sum

alg.
1. initialize an empty set mult7_11 = {}
2. numer % 7 // 1 == integer. 
   add to set,  7 * i in range(integer) ()
3. number % 11
    same
4. return sum of mult7_11
'''

# def seven_eleven(number):
#     mult7_11 = set()
#     for i in range((number // 7) +1):
#         if 7 * i < number:
#             mult7_11.add(7 * i) 
        
#     for i in range((number // 11) +1):
#         if 11 * i < number:
#             mult7_11.add(11 * i) 
        
#     return sum(mult7_11)

# print(seven_eleven(10) == 7)
# print(seven_eleven(11) == 7)
# print(seven_eleven(12) == 18)
# print(seven_eleven(25) == 75)
# print(seven_eleven(100) == 1153)
# print(seven_eleven(0) == 0)
# print(seven_eleven(-100) == 0)

# pp15
'''
input string of numeric digits
output: integer, representing highest possibl product of 4 consecutive numbers

explicit. always 4 or more digits in arg. 

DS: string slicing and int constructor funtions

alg. 
initialize max variable = 0
iterate through the string in slices of four
    iterate in a range of 0 to -4
    if result > max update max

'''
# def greatest_product(numbers):
#     max_product = 0

#     for i in range(len(numbers) - 3):
#         result = int(numbers[i]) * int(numbers[i + 1]) * int(numbers[i + 2]) * int(numbers[i + 3])
#         if result > max_product:
#             max_product = result

#     return max_product

# print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
# print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
# print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
# print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# pp16
'''
input: string
output: integer representing the number of non-unique alphanum characters

ecplicit: only alpha num characters
implicitno empty test

DS iterate through string with count > 1 upticking counter

alg. 
1. initialize result = 0 
2. iterate through string.
3. for each character in the string that occurs more than once, update the result
4. return result
'''

# def distinct_multiples(alphanums):
#     lower_string = alphanums.casefold()
#     result = 0
#     checked = ''
#     for char in lower_string:
#         if lower_string.count(char) > 1 and char not in checked:
#             checked += char
#             result += 1
            
#     return result

# print(distinct_multiples('xyz') == 0)               # (none)
# print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
# print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
# print(distinct_multiples('unununium') == 2)         # u, n
# print(distinct_multiples('multiplicity') == 3)      # l, t, i
# print(distinct_multiples('7657') == 1)              # 7
# print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
# print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# pp17
'''
input list of integers
output: the single number integer needed to bring the sum to a prime number

explicit: alays will contain at least 2 integers, all positive and nonzero, can repeat
implicit: to calculate the next prime, only simple way without looking up imports is to add 1 
and keep checking if prime. 


'''
# from sympy import isprime

# def nearest_prime_sum(list_nums):
#     x = 1
#     while isprime(sum(list_nums) + x) is False:
#         x += 1

#     return x

# print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
# print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
# print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
# print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# # Nearest prime to 163 is 167
# print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

#pp18
'''
input list of integers
output: the index at which all numbers before sum and equal to the sum of all numbers after.

explicit. if no answer, return -1
        if multiple solutions, return the lowest index (i.e. first occurance)
        tyhe sum of numbvers before index 0 or after the last element should be calculated as 0

DS: comparing slices of sequences

alg. 
1. initialize variables left sum = 0 and right sum = 0 
2. iterate through the range of indexes in the sequence.
    a. at each index update left and right sum to equal the sum of the preceding slice and subsequent slice
3. check if left_sum == right_sum
4. if equal, return index.
'''
# def equal_sum_index(numbers):
#     for idx in range(len(numbers)):
#         left_sum = 0
#         right_sum = 0
#         if idx == 0:
#             right_sum = sum(numbers[1:])
#         elif idx == len(numbers) - 1:
#             left_sum = sum(numbers[:-1])
#         else:
#             right_sum = sum(numbers[idx + 1:])
#             left_sum = sum(numbers[:idx])
#         if left_sum == right_sum:
#             return idx
        
#     return -1

# print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
# print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
# print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
# print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# # The following test case could return 0 or 3. Since we're
# # supposed to return the smallest correct index, the correct
# # return value is 0.
# print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

# pp19
'''
input: list of integers
output: the intgger that apears an odd number of times
'''

# def odd_fellow(numbers):
#     for num in numbers:
#         if numbers.count(num) % 2 != 0:
#             return num
        
# print(odd_fellow([4]) == 4)
# print(odd_fellow([7, 99, 7, 51, 99]) == 51)
# print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
# print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
# print(odd_fellow([0, 0, 0]) == 0)

# pp20
'''
input: list of numbers
'''
# def what_is_different(numbers):
#     for num in numbers:
#         if numbers.count(num) == 1:
#             return num
        
# print(what_is_different([0, 1, 0]) == 1)
# print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
# print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
# print(what_is_different([3, 4, 4, 4]) == 3)
# print(what_is_different([4, 4, 4, 3]) == 3)




