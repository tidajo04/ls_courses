# PP1 ROTATION
'''
input: a list of elements
output a NEW list (rotated)

explicit: 
    a new list must be created (without mnodifying the original)
    if input is an empty list, return an empty list
    if input is not a list, return None
    "rotating" means to take the first index of the list and move it to the last index of the new list
    a single element will just return a new list of the single element
implicit: 
    the list can contain any type of element and can be a mix of them

DONT FORGET
    empty argument or any argument that is not a list must return None
    empty list must return an empty list

algorithm
    define function 'rotate_list'
    create an empty list 'new_list'
    create exception for non-list = None
    using slicing, append all but the first index of the list to the new list
    then append the first element of the list to the new list
    return new list (should fulfill if emptry return empty due to step 2)


'''

# def rotate_list(lst):
#     new_list = []

#     if type(lst) != list:
#         return None
#     elif lst == []:
#         return lst
#     else:
#         for idx in range(1, len(lst)):
#             new_list.append(lst[idx])
#         new_list.append(lst[0])

#     return new_list
#passes, but suggested solution is more efficient

# def rotate_list(lst):
#     if not isinstance(lst, list):
#         return None

#     if len(lst) == 0:
#         return []

#     return lst[1:] + [lst[0]]

# # All of these examples should print True

# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])

# PP2 roataion p2
''' 
input an integer, another integer representing the count from the end
output an integer (rotated)

explicit: all inputs are integers
implicit: do not need to account for counts that exceed the number of digits in the first integer

Rules:
    the first argument is the item to be have its digits moved around
    the second argument tells me how far counting from the right to go
    the 'counted' digit is to be removed from its place and placed at the end
    the rest slide left.

algorithm
    define function 'rotate_rightmost_digits' with 2 arguments
    convert number to an iterable
        to string
        to list
    pass the count arg through the pop method .pop(-count) to simultaniously remove the number 
    and return it to the end
    
    join the list back together
    convert baCK TO int


'''
# def rotate_rightmost_digits(number, count):
#     listed_num = list(str(number))
#     listed_num.append(listed_num.pop(-count))

#     return int(''.join(listed_num))

# print(rotate_rightmost_digits(735291, 2) == 735219)  # True
# print(rotate_rightmost_digits(735291, 3) == 735912)  # True
# print(rotate_rightmost_digits(735291, 1) == 735291)  # True
# print(rotate_rightmost_digits(735291, 4) == 732915)  # True
# print(rotate_rightmost_digits(735291, 5) == 752913)  # True
# print(rotate_rightmost_digits(735291, 6) == 352917)  # True
# print(rotate_rightmost_digits(1200, 3) == 1002)      # True

# def max_rotation(number):
#     listed_num = list(str(number))

#     for num in range(len(listed_num) - 1):
#         listed_num.append(listed_num.pop(num))

#     return int(''.join(listed_num))
    

# print(max_rotation(735291) == 321579)          # True
# print(max_rotation(3) == 3)                    # True
# print(max_rotation(35) == 53)                  # True
# print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
# print(max_rotation(105) == 15)                 # True

# PP4 STACK MACHINE INTERPRETATION

'''
input: 
    a string, where each token in the string represents an opperation to be enacted on the values:
        'n' = an integer: place n in the register (do not modify the stack)
        PUSH = push the current register value onto the stack (leave the value in the register)
        ADD = pop a value from the stack and add it to the register value, storing the result in the register
        SUB = pop ... and subtract it from the register value, ...
        MULT = pop ... and multiply it by the register value, ...
        DIV: = pop ... and divide the register value by the popped value, .storing the 'integer' value ...
        REMAINDER = pop ... and divide the register value by the popped value, stroing the integer remainder...
        POP = remove the topmost value from the stack and place it in the register (replaces whatever was in the reg)
        PRINT = print the register value.
output:
        if the string ends in PRINT, the output is the value produced from the PRINT opperation
        otherwise, nothin is printed. ... no output

explicit:
    the stack it the list of values (starts as [])
    the register is the stored value that mutates by various opperations (starts as '0')
        an input of just PRINT would output 0
    can assume all commands will be valid


algorithm:
    define a function for each of the opperations
        create a dictionary with the opperation names as the keys and functions as the value.
            see instruction above for each function
    define the 'minilang' function
        1. initiate 'stack' as []
        2. initiate 'register' as 0
        3. split the input string into a list of words
        4. iterate through the list of words, executing the corresponding function for each iteration
            a. feed the string value of each iteration as the argument for the opperation function
                use an if statement to check what the token is to decide what function to use
                    to check if 'n' : if isinstance(int(token), int) set 'n' as the register
                    else, reference the matching dict 
        5. no return needed (default None) as only the PRINT opperation has a value to return



'''

# def minilang(string=None):

#     if string is None:
#         print('Error: no argument given')
#         return None
    
#     stack = []
#     register = 0

#     opperation_list = string.split(' ')

#     def stack_populated(stack, opperation):
#         if not stack:
#             print(f'Error: Stack is empty - Cannot {opperation}')
#             return False
#         return True

#     for token in opperation_list:
        
#         try:
#             register = int(token)
#         except ValueError:
#             if token == 'PUSH':
#                 stack.append(register)
#             elif token == 'ADD':
#                 if stack_populated(stack, token):
#                     register += stack.pop()
#             elif token == 'SUB':
#                 if stack_populated(stack, token):
#                     register -= stack.pop()
#             elif token == 'MULT':
#                 if stack_populated(stack, token):
#                     register *= stack.pop()
#             elif token == 'DIV':
#                 if stack_populated(stack, token):
#                     register /= stack.pop()
#                     register = int(register)
#             elif token == 'REMAINDER':
#                 if stack_populated(stack, token):
#                     register %= stack.pop()
#                     register = int(register)
#             elif token == 'POP':
#                 if stack_populated(stack, token):
#                     register = stack.pop()
#             elif token == 'PRINT':
#                 print(register)
#             else:
#                 print("input error")
       
    
# minilang('MULT DIV PUSH PRINT')
# minilang()
# minilang('print')
# # # 0

# minilang('5 PUSH 3 MULT PRINT')
# # 15

# minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

# minilang('5 PUSH POP PRINT')
# # 5

# minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

# minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

# minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

# minilang('-3 PUSH 5 SUB PRINT')
# # 8

# minilang('6 PUSH')
# # (nothing is printed)

# PP5 Word to Digit

'''
input string
output similar string with word-numbers replaced with digits.

explicit: may assume no punctuation, 
implicit: only dealing with 0-9

ds convert strings to lists and check for in dictionary then convert back to string.

algorithm:
    create dictionary of number-words to digit values
    split string into words
    iterate through list checking if word is in dictionary
        if in dictionary, replace word with dictionary value
    join list 
    return new string

'''

# def word_to_digit(string):
#     WORD_NUM = {
#         'one': '1',
#         'two': '2',
#         'three': '3',
#         'four': '4',
#         'five': '5', 
#         'six': '6', 
#         'seven': '7', 
#         'eight': '8', 
#         'nine': '9', 
#         'zero': '0'
#         }
    
#     # import re

#     # listed_string = re.findall(r'\w+|[^\w\s]', string)
#     # new_list = []
    
#     # for word in listed_string:
#     #     new_list.append(WORD_NUM.get(word, word))
        
#     # result = ''
#     # for idx, word in enumerate(new_list):
#     #     if idx > 0 and re.match(r'\w', word):
#     #         result += ' '
#     #     result += word
    
#     # return result
# ###OR
#     for word in WORD_NUM:
#         string = string.replace(word, WORD_NUM[word])

#     return string
    

    

# message = 'Please call me... at five, five, five, one, two, three, four. highfive'
# print(word_to_digit(message))# == "Please call me at 5 5 5 1 2 3 4")
# # Should print True

# PP6 IS IT PRIME

'''
input: positive integer
output boolean (T = prime)

explicit: prime number 1 and sefl, excludes 1

ds: math and range iteration ?

alg. 
    look at the range of numbers up to number given
    use modulo on each iteration to determin if whole number
    if modula 1 is 0, it is whole number
    append the result to 'divisor' l;ist
    if divisor list length is 2, then prime.

'''

# def is_prime(number):
#     divisor = []
    
#     for num in range(1, number + 1):
#         if (number / num) % 1 == 0:
#             divisor.append(num)
    
#     if len(divisor) == 2:
#         return True
#     else:
#         return False

# # print(is_prime(1) == False)              # True
# # print(is_prime(2) == True)               # True
# # print(is_prime(3) == True)               # True
# # print(is_prime(4) == False)              # True
# # print(is_prime(5) == True)               # True
# # print(is_prime(6) == False)              # True
# # print(is_prime(7) == True)               # True
# # print(is_prime(8) == False)              # True
# # print(is_prime(9) == False)              # True
# # print(is_prime(10) == False)             # True
# # print(is_prime(23) == True)              # True
# # print(is_prime(24) == False)             # True
# # print(is_prime(997) == True)             # True
# # print(is_prime(998) == False)            # True
# # print(is_prime(3_297_061) == True)       # True
# print(is_prime(23297061) == False)     # True

# PP7 FIBONACCI NUMBERS (procedural)
'''
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)
'''

# def fibonacci(nth):
#     F_list = [1, 1] #sets the starting 2

#     for n in range(nth -2): # forces the sequence to loop the necessary number of times
#         F_list.append(F_list[-1]+ F_list[-2]) #each loop appends the sum of the last two 

#     return F_list[-1] #outputs the last number in the list


# print(fibonacci(1) == 1)                  # True
# print(fibonacci(2) == 1)                  # True
# print(fibonacci(3) == 2)                  # True
# print(fibonacci(4) == 3)                  # True
# print(fibonacci(5) == 5)                  # True
# print(fibonacci(6) == 8)                  # True
# print(fibonacci(12) == 144)               # True
# print(fibonacci(20) == 6765)              # True
# print(fibonacci(50) == 12586269025)       # True
# print(fibonacci(75) == 2111485077978050)  # True

# PP8 FIBONACCI NUMBERS (RECURSION)

# def fibonacci(nth):
#     if nth <= 2:
#         return 1
    
#     return fibonacci(nth - 1) + fibonacci(nth - 2)

# PP9 FIBONACCIE (MEMOIZATION)
# import sys

# sys.set_int_max_str_digits(50_000)

# memo = {}
# def fibonacci(nth):
#     if nth <= 2:
#         return 1
#     elif nth in memo:
#         return memo[nth]
#     else:
#         memo[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
#         return memo[nth]
    
# def find_fibonacci_index_by_length(idx):
#     nth = 3

#     while len(str(fibonacci(nth))) <= idx:
#         fibonacci(nth)
#         nth += 1

#     for nth, f_num in memo.items():
#         if len(str(f_num)) == idx:
#             return nth
        
# # All of these examples should print True
# # The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
# print(find_fibonacci_index_by_length(2) == 7)
# print(find_fibonacci_index_by_length(3) == 12)
# print(find_fibonacci_index_by_length(10) == 45)
# print(find_fibonacci_index_by_length(16) == 74)
# print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)

# # Next example might take a little while on older systems
# print(find_fibonacci_index_by_length(10000) == 47847)