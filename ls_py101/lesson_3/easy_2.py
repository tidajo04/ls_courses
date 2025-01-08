#question1
# numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
# # print(numbers[::-1])
# print(list(reversed(numbers)))

# question2
# numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

# number1 = 8  # False (not in numbers)
# number2 = 95 # True (in numbers)

# print(number1 in numbers)
# print(number2 in numbers)

# question3
# print(43 in range(10, 101))
# print(100 in range(10, 101))
# print(101 in range(10, 101))

# question4
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [1, 2, 3, 4, 5]

# del numbers1[2]
# #or
# numbers2.pop(2)
# print(numbers1)
# print(numbers2)
# # using pop creates a return value so one could use it as a variable
# # while using del does not create a return value.
# print(numbers2.pop(2))
# print(numbers2)

# question5
# numbers = [1, 2, 3, 4]
# table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# print(isinstance(numbers, list), isinstance(table, list))

# #or
# type(numbers) is list
# type(table) is list

# question6
# title = "Flintstone Family Members"

# print(title.center(40))

# question7
# statement1 = "The Flintstones Rock!"
# statement2 = "Easy come, easy go."

# def char_count(letter, string):
#     counter = 0
#     for letter in string:
#         if letter == "t":
#             counter += 1
#     print(counter)

# char_count('t', statement1)
# char_count('t', statement2)

# #aparently another prebuilt exists. could just use .count('t')

# print(statement2.count('t'))

# #question8
# ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

# # print('Spot' in ages)

# ages['Marilyn'] = 22
# ages['Spot'] = 237
# # or use .update
# ages.update({'Marilyn': 22, 'Spot': 237})
# print(ages)





        