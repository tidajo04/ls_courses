#"""question 1: 
    # Answer, no, it will be [1, 2, 5] 
    # Wrong, will raisew error because out of range.
        #  I was thinking about the index looping back over once it goes to the end, 
        # but that only happens with specific tools like itertool. Normally
        # idices only go to the final item (can also use negatives up to the first)

#question 2
# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False
# #original answer:
# def ends_with(str, symbol):
#     print(True) if str[-1] == symbol else print(False)

# ends_with(str1, "!")
# ends_with(str2, "!")
# #suggested answer (forgot a premade function exists)
# print(str1.endswith('!'))
# print(str2.endswith('!'))

# question3
# famous_words = "seven years ago..."
# pre_words = 'For score and'

# phrase = f"{pre_words} {famous_words}"
# phrase2 = pre_words + ' ' + famous_words
# phrase3 = [pre_words, famous_words]

# print(phrase)
# print(phrase2)
# print(' '.join(phrase3))

#question 4
# munsters_description = "the Munsters are CREEPY and Spooky."

# print(munsters_description.capitalize())

#question 5
# print(munsters_description.swapcase())

#question 6
# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# def word_in(word, string):
#     print('yes') if word in string else print('no')

# word_in("Dino", str1)
# word_in("Dino", str2)

# print('Dino' in str1) 

# question 7
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones += ['Dino']
# #OR
# flintstones.append('Dino')
# print(flintstones)

# question 8
# flintstones += ['Dino', 'Hoppy']
# #or 
# flintstones.extend(["Dino", 'Hoppy'])
# print(flintstones)

# question9
# advice = "Few things in life are as important as house training your pet dinosaur."

# print(advice.split('house')[0])

# question10
# print(advice.replace('important', 'urgent'))
