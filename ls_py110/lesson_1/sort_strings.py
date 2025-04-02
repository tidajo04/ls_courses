'''
Given a list of strings, sort the list based on the highest number of 
adjacent consonants a string contains and return the sorted list. 
If two strings contain the same highest number of adjacent consonants, 
they should retain their original order in relation to each other. 
Consonants are considered adjacent if they are next to each other in the 
same word or if there is a space between two consonants in adjacent words.

-inputs: a list of strings.
-output: the same list, sorted with the strings in the order of highest 
         number of adjacent consonencts

-Explicit rules: 
    -"adjacent consonents" are any consonent is next to another (ignoring whitespace)
    - if two strings have the same number of Adj Cons. the order should remain the same among them
    
-implicit
    - a sting may be a single word or multiple words
    - should punctuation be ignored?

-questions:
    - can a string be empty
    - can there be punctuation (i.e. does punctuation count as a space?)
    - ascending order or decending
    - when counting, does this mean consecutively adjacent or total. 
        i.e. tttaatt ... is this 3 or 5?

- DATA STRUCTURE:
pretty simple. we are working with lists and soprting the same lists. my need to use a dictionary to keep track of the ewlements

ALGORITHM
- 1. take each element of the given list and run it through a function that counts the 
    number of adjacent consonents
        - initiate a count
        - run each letter through a "is_consonent" function 
            --define consonents, to include all cases
            --check if the input is in the list (true or false)
        - join the characters to remove whitespace
        - if a letter is a consonent, check it against the previous letter
        - if the previous letter is consonent, increment counter by 1
        - if counter > 0, increment counter by 1
        
- 2. sort the elements of the list in the proposed order (using (key=function))
- 3. return the same list with the new order.
'''

# def sort_by_consonant_count(list_input):
#     list_input.sort(key=consonant_counter, reverse=True)
#     return list_input

# def consonant_counter(string):
#     count = 0 
#     string = ''.join(string.split())
#     consonants = 'bcdfghjklmnpqrstvwxyz'
#     for i in range(1, len(string)):
#         if string[i] in consonants and string[i-1] in consonants:
#             count +=1
    
#     return count
    

# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']