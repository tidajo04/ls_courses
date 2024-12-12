name_list = {
    'Alice'.casefold():     'USA'.casefold(),  #casefold on each name allows for case insensitivity on the user input
    'Francios'.casefold():  'Canada'.casefold(), 
    'Inti'.casefold():      'Peru'.casefold(), 
    'Monika'.casefold():    'Germany'.casefold(), 
    'Sanyu'.casefold():     'Uganda'.casefold(), 
    'Yoshitaka'.casefold(): 'Japan'.casefold(), 
    }

user = name_list.keys()
country = name_list.values()

name = input('What is your name? ').casefold() #casefold matches input to key

if name in name_list:
    print(f'{name.capitalize()} is from {name_list[name]}') # checks if name is within list 
else:                                                       # also capitalized reply regardless of input        
    print(f'{name.capitalize()} is not within the database.')

if name not in name_list:
    new_country = input('Please type in your country of origin to be added to the database: ').casefold()
    name_list[name.casefold()] = new_country


print(f'Thank you, {name.capitalize()}. You have been added to our database')

import pprint
pprint.pprint(name_list)



