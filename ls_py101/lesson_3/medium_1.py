# string = 'The Flintstones Rock!'

# def doodle(string, num, symbol):
#     count = 0
#     while count < num:
#         string = symbol + string
#         print(string)
#         count += 1

# doodle(string, 10, '-')

# # alt (LS solution)
# for padding in range(1, 11):
#     print(f'{'-' * padding}The Flintstones Rock!')

# question2
# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# print(factors(-100))

# question3
# one mutates the list, the other creates a new list and then reassigns

# question 4 - 6 (simple answers)

# question 7
# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }

# def mess_with_demographics(demo_dict):
#     for key, value in demo_dict.items():
#         value["age"] += 42
#         value["gender"] = "other"

# mess_with_demographics(munsters)

# print(munsters)

# question8

