# # PP1 - Searching 101
# # order = ['1st', '2nd', '3rd', '4th', '5th', 'last']
# # num_list = []
# # for _ in order:
# #     response = input(f'Enter the {_} number: ')
# #     num_list.append(response)

# # if num_list[-1] in num_list[:-1]:
# #     print(f'{num_list[-1]} is in {','.join(num_list[:-1])}.')
# # else:
# #     print(f'{num_list[-1]} isn\'t in {','.join(num_list[:-1])}.')
    
# #PP2 Palindromatic Strings p1

# # def is_palindrome(string):
# #     return string == string[-1::-1]
       
    
# # # All of these examples should print True

# # print(is_palindrome('madam') == True)
# # print(is_palindrome('356653') == True)
# # print(is_palindrome('356635') == False)

# # # case matters
# # print(is_palindrome('Madam') == False)

# # # all characters matter
# # print(is_palindrome("madam i'm adam") == False)

# # PP3 palindromatic syndrom p2
# # def is_real_palindrome(string):
# #     cleaned_string = ''
# #     for i in string:
# #         if i.isalnum():
# #             cleaned_string += i
# #     return cleaned_string.casefold() == cleaned_string[-1::-1].casefold()

# # print(is_real_palindrome('madam') == True)           # True
# # print(is_real_palindrome('356653') == True)          # True
# # print(is_real_palindrome('356635') == False)         # True
# # print(is_real_palindrome('356a653') == True)         # True
# # print(is_real_palindrome('123ab321') == False)       # True

# # # case doesn't matter
# # print(is_real_palindrome('Madam') == True)           # True

# # # only alphanumerics matter
# # print(is_real_palindrome("Madam, I'm Adam") == True) # True

# # PP4 Running Totals
# # def running_total(num_lst):
# #     r_total_lst = []
# #     total = 0

# #     for num in num_lst:
# #         r_total_lst.append(total + num)
# #         total += num
            
# #     return r_total_lst

# # print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# # print(running_total([14, 11, 7, 15, 20])
# #       == [14, 25, 32, 47, 67])                    # True
# # print(running_total([3]) == [3])                  # True
# # print(running_total([]) == [])                    # True

# # PP5 letter counter

# # def word_sizes(s):
# #     word_size = {}
# #     for word in s.split():
# #         if len(word) in word_size:
# #             word_size[len(word)] += 1
# #         else:
# #             word_size[len(word)] = 1

# #     return word_size

# # # All of these examples should print True

# # string = 'Four score and seven.'
# # print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# # string = 'Hey diddle diddle, the cat and the fiddle!'
# # print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# # string = 'Humpty Dumpty sat on a wall'
# # print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# # string = "What's up doc?"
# # print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# # print(word_sizes('') == {})

# # PP6
# def word_sizes(s):
#     word_size = {}
#     cleaned_words = []

#     for word in s.split():
#         cleaned_word = ''
#         for i in word:
#             if i.isalpha():
#                 cleaned_word += i
#         cleaned_words.append(cleaned_word)

#     for word in cleaned_words:
#         if len(word) in word_size:
#             word_size[len(word)] += 1
#         else:
#             word_size[len(word)] = 1

#     return word_size

# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})