# ex 1
# print(len("These aren't the droids you're looking for."))
# # ex 2
# print('string'.upper())
# ex 3
# print('Roger'.casefold() == 'RoGeR'.casefold())
# print('Roger'== 'RoGeR')
# ex 4
# poem = """A pirate I was meant to be!
# Trim the sails and roam the sea!"""        

# print(poem)
# ex5
# char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
# print('x' in char_sequence)
# ex 6
# def is_empty_or_blank(string): 
#     return len(string) == 0

# print(is_empty_or_blank('mars'))
# print(is_empty_or_blank(''))
# ex 7
# def is_empty_or_blank(string): 
#     return len(string.strip(' ')) == 0

# print(is_empty_or_blank('mars'))
# print(is_empty_or_blank(''))
# print(is_empty_or_blank('  '))
# ex 8
# string = 'launch school tech & talk'
# print(string.title())
# ex 9
# def starts_with(word, pref):
#     return True if word[0:len(pref)] == pref else False


# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

# # alternative 
# def starts_with(word, pref):
#     return word.startswith(pref) #also a .endswith functions pre-exists
    
# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch")) 
# ex10
# def count_substrings(string, sub):
#     return string.count(sub)

# print(count_substrings("lemon lemon lemon", "lemon")) # 3
# print(count_substrings("laLAlaLA", "la")) # 2
# print(count_substrings("launch", "uno")) # 0