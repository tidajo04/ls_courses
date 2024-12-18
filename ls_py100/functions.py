# ex 1
# def multiply(num1, num2):
#     return num1 * num2
# ex 2
# def bruce_eckel_quote():
#     print('Python is executable psuedocode.')
# # ex 3
# def cite(author, quote):
#     print(f'{author} said: "{quote}"')
# ex 4
# def squared_number(num):
#     return num**2
# ex 5
# def multiples_of_three():
#     divisor = 1

#     for dividend in range(3, 31, 3):
#         print(f'{dividend} / {divisor} = 3')
#         divisor += 1

# multiples_of_three()
# ex 6
# def compare_length(string1, string2)
#     if len(string1) < len(string2):
#         return -1
#     elif len(string1) > len(string2):
#         return 1
#     else:
#         return 0
# ex 7
# print('Captain Ruby'.replace('Ruby', 'Python'))
# ex 8
# ISO_dict = {'en': "Hi", 'fr': 'Salut', 'pt': "Ola"}

# def greet(lang):
#     return f'{ISO_dict[lang]}!'

# print(greet('en'))
# print(greet('fr'))
# print(greet('pt'))
# ex 9
# def extract_language(locale):
#     return locale[:2]

# print(extract_language('en_US.UTF-8'))
# ex 10
# def extract_language(locale):
#     return locale[3:5]

# print(extract_language('en_US.UTF-8'))
ISO_dict = {'en': 'Hi', 
            'fr': 'Salut', 
            'pt': 'Ola',
            'de': 'Hallo',
            'sv': 'Hej',
            'af': 'Haai'
            }
import re

locale_input = input('Please input your locale. ')

def greet(lang):
    return f'{ISO_dict[lang]}!'

def extract_locale(locale):
    return re.split(r'[_.-]', {locale})

def local_greet(locale):
    return greet(extract_locale(locale)[0])

print(local_greet(locale_input))
