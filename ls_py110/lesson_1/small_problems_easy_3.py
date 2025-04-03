# PP1 AFTER MIDNIGHT P1
'''
input - any integer
output - a string "hh:dd"

explicit
    all number input will be integers
    "time" string will always be 2 decimal places representing the hour and 2 the minutes
    using military time
implicit 
    1440 minutes in a day, but includes 0, so 0 through 1339 is the range

data structures:strings, and ranges

alg
    define function
    set 'time' variable to 0
    calculate the difference
        subtract (or add if negative) 60 until the remainder would be less than 60
            set the number of times this repeats to be the 'hours' variable
            set this remainder as the 'minutes' variable
        if the 'hours' variable is grater than 23 subrtact (or add if negative) 24 until the remainder would be less than 24
            repeat until 'hours' is less than 24
            set the hours' variable to what is left
    format hours and minutes to always have two places
    return interpolated string (changing numbers to strings)

'''
# def time_of_day(number):
    
#     hours = 0
#     minutes = number
#     if minutes > 0:
#         while minutes > 59:
#             minutes -= 60
#             hours += 1
#         while hours > 23:
#             hours -= 24
#     elif minutes < 0:
#         while minutes < -59:
#             minutes += 60
#             hours += 1
#         minutes = 60 + minutes
#         while hours > 23:
#             hours -= 24
#         hours = 23 - hours
#     else:
#         minutes = 0
#         hours = 0
    
#     return f'{hours:02d}:{minutes:02d}'

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

#PP2 AFTER MIDNIGHT p2

# def after_midnight(string):
#     hour_min = string.split(":")
    
#     if hour_min[0] == "24":
#         minutes = 0
#     else:
#         minutes = (int(hour_min[0]) * 60) + int(hour_min[1])
    
#     return minutes

# def before_midnight(string):
#     hour_min = string.split(":")
    
#     if hour_min[0] == "24":
#         minutes = 0
#     else:
#         minutes = (int(hour_min[0]) * 60) - int(hour_min[1])
    
#     return minutes

# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

# PP3 DOUBLE CHAR p1
# def repeater(string):
#     new_string = ''
#     for char in string:
#         new_string += char * 2
#     return new_string

# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

# PP4 SOUBLE CHAR p2
# def double_consonants(string):
#     new_string = ''
#     for char in string:
#         if char.casefold() in 'bcdfghjklmnpqrstvwxyz':
#             new_string += char * 2
#         else: 
#             new_string += char
#     return new_string

# # All of these examples should print True
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

# PP5 REVERSE NUMBER
# def reverse_number(number):
#     return int(str(number)[::-1])
    
# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

# PP6 COUNTING UP
# def sequence(number):
#     return list(range(1, number + 1))

# print(sequence(5) == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

# PP7 NAME SWAPPING
# def swap_name(name):
#     return ', '.join(name.split()[::-1])

# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# PP8 SEQUENCE COUNTING
'''
input: two integers, first is a count, second the starting integer of sequence
output: list containing the 'count' number of elements starting with the 'start' 
        number and each thereafter being a multiple of the start.

explicit
    can be any interger
    a count of 0 should output an empty list

DS list construction.

alg.
    1. init an empty 'seq_list'
    2iterate through a range of the 'count' 
        for ewach iteration, multiply the starting number by it +1
    3. return the 'seq_list'
'''
# def sequence(num1, num2):
    
#     return [num2 * num for num in range(1, num1 +1)]

# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True

# PP9 REVERSED LISTS
# def reverse_list(lst):
#     for index in range(len(lst)):
#         lst.insert(index, lst.pop())
#     return lst

# list1 = [1, 2, 3, 4]
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True

# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True

# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True

# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

# PP10 MATCHING PARENTHISIS
'''
input: a string
output: Boolean is all parenthisis are properly 'paired'

explicit: 
    a parenth is pairs if it each '(' has a subsequent coresponding ')' 
    no parenth should retun True
    unmatched returns False

data structure: could stay with string iteration

alg:
    ... for each 'open' must have a subsequent 'close' and at the end open == close
    1. iterate through string
        once an 'open' is found and to 'open' count, 
            continue the iteration until a 'close' is found and add to count.
        continue iteration (form last open) and repeat
    2. check if open == close
    

'''

# def is_balanced(string):
#     open_index = []
#     close_index = []
#     order_check = ''

#     for index in range(len(string)):
#         if string[index] == '(':
#             open_index.append(index)
            
#     for index in range(len(string)):
#         if string[index] == ')':
#             close_index.append(index)

#     if len(open_index) == len(close_index):
#         for index in range(len(open_index)):
#             if open_index[index] < close_index[index]:
#                 continue
#             else:
#                 order_check += "fail"
#                 break
    
#     return True if len(open_index) == len(close_index) and order_check != 'fail' else False

    
# print(is_balanced("What (is) this?") == True)        # True
# print(is_balanced("What is) this?") == False)        # True
# print(is_balanced("What (is this?") == False)        # True
# print(is_balanced("((What) (is this))?") == True)    # True
# print(is_balanced("((What)) (is this))?") == False)  # True
# print(is_balanced("Hey!") == True)                   # True
# print(is_balanced(")Hey!(") == False)                # True
# print(is_balanced("What ((is))) up(") == False)      # True