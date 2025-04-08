# PP1 CUTE ANGLES 
'''
input: a float between 0 and 360
output: a string xx^XX'xx"

explicit: 
    the number will be a float or integer between 0 and 360

data structures: interpolated string construction with arithmatic opperations through floats

algorithm:
    initialize the DEGREE symbol

    math:
        1 set a counters to 1
            num for the current working number (float)
            counter for iteration number (int)
            sign for assignment of sign (list)
        1.5 open a loop that ends if counter is more than 3
        2 use X.xx - .xx to return the whole number
            set to 'degrees'
        3 use X.xx % X to return the decimal place only 
            set to 'decimal_minute
        4 divide 'decimal_minute' by 60 to get a new float number
            update number as the new number
        5 increment 'counter'
        6 repeat steps 2 - 5 
            *this will get a new whole number to be set as the 'minutes' 
            (the 2nd loop) and will return the 'seconds' (the 3rd loop)
        5. end the loop after 3 iterations

    return a, f string (f"{degrees}{DEGREE}{minutes}'{seconds}\"")
'''

# def dms(number):
#     DEGREE = "\u00B0"
#     counter = 0
#     num = number
#     sign = ['degrees', 'minutes', 'seconds']
#     while counter < 3:
#         if num != 0:
#             sign[counter] = num // 1 
#             num = num % round(sign[counter], 2)
#             counter += 1
#             if counter > 2:
#                 break
#             sign[counter] = round((num * 60), 2)
#             num = sign[counter]
#         else: 
#             sign[counter] = round(0, 2)
#             counter += 1
    
#     for index in range(len(sign)):
#         over_under = abs(sign[0] // 360)
#         if sign[index] > 360:
#             sign[index] -= (360 * over_under)
#         if sign[index] < 0:
#             sign[index] += (360 * over_under)
    
#     return f"{int(sign[0])}{DEGREE}{int(sign[1]):02}'{int(sign[2]):02}\""

# # All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# print(dms(-1))   # 359°00'00"
# print(dms(400))  # 40°00'00"
# print(dms(-40))  # 320°00'00"
# print(dms(-420)) # 300°00'00"
# print(dms(-730))
# print(dms(990))

# PP2 COMBINING LISTS
# def union(lst_1, lst_2):
#     union_list = set(lst_1) | set(lst_2)
#     return union_list

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

#PP3 HALVSIES
'''
input: list
output: list with 2 lists as elements

explicit: 
    all elements are lists
    odd numbers should be split where 1st element contains middle
    if 1 element, the s3econd list will be blank
    if no elements, both output elements will be blank lists

DS: lists only
Alg:
    define function 'halvsies'
    remove elements from the end of the list and fill them into a second list
    when the first list is equal to or greater than the second, stop
    return a list of the two new lists

'''
# def halvsies(my_list):
#     list_1 = []
#     list_2 = my_list

#     while len(list_1) < len(list_2):
#         list_1.append(list_2.pop(0))

#     return [list_1, list_2]

# # All of these examples should print True
# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

# PP4 Find Duplicate
# def find_dup(lst):

#     for i in lst:
#         if lst.count(i) == 2:
#             return i
     


# print(find_dup([1, 5, 3, 1]) == 1) # True
# print(find_dup([
#                   18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
#                   38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
#                   14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
#                   78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
#                   89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
#                   41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
#                   55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
#                   85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
#                   40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
#                    7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
#               ]) == 73)       # True
# PP5 Combine two lists
# def interleave(list_1, list_2):
#     new_list = []
#     while len(list_1) or len(list_2) > 0:
#         new_list.append(list_1.pop(0))
#         new_list.append(list_2.pop(0))
#     return new_list

    

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave(list1, list2))# == expected)      # True

# PP6 MULTIPLICATIVE AVERAGE
'''
input: list of positivve integers
output: a string (number rounded to 3 dec.)

explicit:
    all numbers are non-zero positive integers
    output needs to cut off value to 3 decimals

DS - list iteration, rounding method, string construction
algorithm
    define function 'multiplicative_average'
    initiate a total at 1
    iterate through each element and multiply by the total
    update the total 
    repeat
    set result as the the total/length of list to string and round it to three places.
'''
# def multiplicative_average(lst):
#     total = 1
#     for i in lst:
#         total *= i

#     result = total / len(lst)
#     return str(f'{result:.3f}')

# # All of these examples should print True
# print(multiplicative_average([3, 5]) == '7.500')
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

# PP7 MULTIPLY LISTS
# def multiply_list(list_1, list_2):
#     new_list = []

#     for index in range(len(list_1)):
#         new_list.append(list_1[index] * list_2[index])
    
#     return new_list

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

#PP8 
# def digit_list(number):
    
#     return [int(digit) for digit in str(number)]

# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                     # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True

# PP9 HOW MANY?
# def count_occurrences(lst):
#     my_set = set()
#     for item in lst:
#         my_set.add((item.casefold(), lst.count(item)))

#     for item, count in my_set:
#         print(f'{item} => {count}')

# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck', 'suv']

# count_occurrences(vehicles)

# PP10 LIST AVERAGE
# def average(lst):
#     total = sum(lst)
#     return total // len(lst)



# print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
# print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
# print(average([7]) == 7)                          # True
    




