# ex 1
# car = {
#     'type': 'sedan', 
#     'color': 'blue', 
#     'mileage': 80_000
#     }
# # ex 2 (cont.)
# car['year'] = 2003
# print(car)
# # ex 3 (cont)
# car.pop('mileage') ## or use del car['mileage']
# print(car)
# # ex 4
# print(car['color'])
# # ex 5
# print(len(car))
# ex 6
# student = {
#     'id': 123,
#     'grade': 'B',
# }
# print('name' in student)
# print('grade' in student)
# # ex 7
# vehicles = {
#                 'car': {
#                     'type' : 'sedan',
#                     'color': 'blue',
#                     'year' : 2003, 
#                 }, 
#                 'truck': {
#                     'type' : 'pickup',
#                     'color': 'red',
#                     'year' : 1998,
#                 }
#             }
# # ex 8
# car = {
#     'type' : 'sedan',
#     'color': 'blue',
#     'year' : 2003, 
# }

# car = [['type', 'sedan'], ['color', 'blue'], ['year', 2003],]
# ex 9
# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }
# new_list = []
# for item in numbers:
#     new_list.append(numbers[item] // 2)

# print(new_list) 
# ex 10
numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

for key, value in numbers.items():
    print(f'A {key} number is {value}')