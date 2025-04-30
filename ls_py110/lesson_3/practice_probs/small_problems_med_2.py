# PP1 LETTERCASE PERCENTAGE RATIO
'''
input - string
output - return dictionay
    % of chars lowercase
    % of chars uppercase
    % of chars niehter (nonalpha)

explicit. 
    no empty strings
    all percentages should return value be strings '0.00' - '100.00'
    values should be rounded to 2 decimal places

implicit
    decimal place values should be 'extended to keep a leading 0

DS string iteration, dictionaries

alg
    1. define function
    2. create empty dictionary
    3. use regex to find the number of [a-z], [A-Z], [^a-z]
    4. convert count to percentage
        count/length of string
        format to 2 de4cimal places
        convert to string value
    5. populate dictionary with formated string percentage
    6. return dictionary

'''
# import re
# def letter_percentages(string):
#     result = {}
#     result['lowercase'] = f'{(len(re.findall(r'[a-z]', string))
#                              / len(string)*100):.2f}'
#     result['uppercase'] = f'{(len(re.findall(r'[A-Z]', string))
#                              / len(string)*100):.2f}'
#     result['neither'] = f'{(len(re.findall(r'([^A-Za-z])', string))
#                              / len(string)*100):.2f}'

#     return result



# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

# PP2 Triangle Sides
'''
input: three integers/floats
output: a string 

explicit:
    have to deal with 0s input
    input may be float or integer
    no side can be 0 (i.e. if an input is zero, invalid)
    the length of the two smallest numbers must > the largest number

        output: isosolese two sides equal
        equilateral: all sides equal
        scalene: no sides equal
        invalid: 0, or L < 2s

data structures:nested if statements should do the trick. 

algorithm: 
    
    2. set up if statements to test each condition
        only 'triocky one will be the length of largest < 2smallest
    3.return result.

'''
# def triangle(side1, side2, side3):
#     sides = [side1, side2, side3]
#     if 0 in (side1, side2, side3):
#         return 'invalid'
#     elif max(sides) > sum(sides) - max(sides):
#         return 'invalid'
#     elif side1 == side2 == side3:
#         return 'equilateral'
#     elif side1 != side2 and side1 != side3 and side2 != side3:
#         return 'scalene'
#     else:
#         return 'isosceles'
    
# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # Trueprint(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0.0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

# PP3 Tri-ANGLES
# def triangle(a1, a2, a3):
#     angle_degrees = [a1, a2, a3]
#     if sum(angle_degrees) != 180 or 0 in angle_degrees:
#         return 'invalid'
#     elif 90 in angle_degrees:
#         return 'right'
#     elif any(angle > 90 for angle in angle_degrees):
#         return 'obtuse'
#     else: 
#         return 'acute'
    
# print(triangle(60, 70, 50) == "acute")      # True
# print(triangle(30, 90, 60) == "right")      # True
# print(triangle(120, 50, 10) == "obtuse")    # True
# print(triangle(0, 90, 90) == "invalid")     # True
# print(triangle(50, 50, 50) == "invalid")    # True

# PP4 ULUCKY DAYS
# from datetime import date

# def friday_the_13ths(year):
#     count_13ths = 0
          
#     for month in range(1, 13):
#         if date(year, month, 13).strftime("%A") == "Friday":
#             count_13ths += 1    
        
#     return count_13ths

# print(friday_the_13ths(1986) == 1)      # True
# print(friday_the_13ths(2015) == 3)      # True
# print(friday_the_13ths(2017) == 2)      # True

# PP5 Next featured number higher than given Value
'''
input: integer
output: integer (next 'featured number')

explicit: 
    'featured number' = 
        odd
        multiple of 7
        all unique digits
implicit: no negatives

DS math while loop, convert to string to check for uniquness.

alg:
    1. def function
    2. set up a while loop 
        check every multiple of seven that is greater than the starting number argument
            if the 7mult matches the rules, return that number
            to check for match:
                check if odd
                convert to string and check for uniquness
                if BOTH true, we found our guy
'''
# def isunique(number):
#         strfnum = str(number)

#         for num in strfnum:
#             if strfnum.count(num) > 1:
#                 return False
#         return True

# def next_featured(number):
#     check = number - number % 7

#     while True:
#         check += 7
#         if check % 2 != 0 and isunique(check) is True:
#             break
#         if check > 9999999999:
#             return error
#     return check

# error = ("There is no possible number that "
#          "fulfills those requirements.")
# print(next_featured(12) == 21)                  # True
# print(next_featured(20) == 21)                  # True
# print(next_featured(21) == 35)                  # True
# print(next_featured(997) == 1029)               # True
# print(next_featured(1029) == 1043)              # True
# print(next_featured(999999) == 1023547)         # True
# print(next_featured(999999987) == 1023456987)   # True
# print(next_featured(9876543186) == 9876543201)  # True
# print(next_featured(9876543200) == 9876543201)  # True
# print(next_featured(9876543201) == error)       # True

# PP6 SUM SQUARE
# def sum_square_difference(number):
#     return sum([num for num in range(number + 1)])**2\
#          - sum([num**2 for num in range(number + 1)])

# print(sum_square_difference(3) == 22)          # True
# # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

# print(sum_square_difference(10) == 2640)       # True
# print(sum_square_difference(1) == 0)           # True
# print(sum_square_difference(100) == 25164150)  # True

# def bubble_sort(lst):
#     while True:
#         check = False
#         for idx in range(len(lst) - 1):     
#             if lst[idx] > lst[idx +1]:
#                 lst[idx], lst[idx+1] = lst[idx +1], lst[idx]
#                 check = True
#         if not check:
#             break
#     return lst
 
# lst1 = [5, 3]
# bubble_sort(lst1)
# print(lst1 == [3, 5])                   # True

# lst2 = [6, 2, 7, 1, 4]
# bubble_sort(lst2)
# print(lst2 == [1, 2, 4, 6, 7])          # True

# lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#         'Kim', 'Bonnie']
# bubble_sort(lst3)

# expected = ["Alice", "Bonnie", "Kim", "Pete",
#             "Rachel", "Sue", "Tyler"]
# print(lst3 == expected)                 # True