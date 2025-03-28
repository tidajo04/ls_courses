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