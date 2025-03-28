#PP1
# fruits = ("apple", "banana", "cherry", "date", "banana")

# print(fruits.count('banana'))

#PP2
# numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers))

# answer 5

# PP3
# a | b

# ages = {
#     "Herman": 32,
#     "Lily": 30,
#     "Grandpa": 5843,
#     "Eddie": 10,
#     "Marilyn": 22,
#     "Spot": 237,
# }

# print(sum(ages.values()))
# print(min(ages.values()))

statement = "The Flintstones Rock"

letter_occurance = {}

for letter in statement:
    if letter in letter_occurance.keys():
        letter_occurance[letter] += 1
    else:
        letter_occurance[letter] = 1

print(letter_occurance)