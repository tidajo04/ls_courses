#PP1 Transpose matrix
'''
input: a nested list 3x3 
output: a formated grouping of integers. (DO NOT MODIF THE ORIGINAL)
    should be the transposition of the nested lists.
    No commas ()

    i need to append the first index of each row to first index of the new list
    then i need to apend the 2nd index of each row to the second index of new list
    eetc
'''
# # matrix = [
# #     [1, 5, 8],
# #     [4, 7, 2],
# #     [3, 9, 6],
# #     [5, 2, 3]
    
# # ]

# def transpose(matrix):
#     new_matrix = [[] for idx in range(len(matrix[0]))]
    
#     for idx in range(len(matrix)):
#         for row in matrix:
#             new_matrix[idx].append(row[idx])

#     return new_matrix
            
# # def transpose(matrix):
# #     transposed = []
# #     new_rows_count = len(matrix[0])

# #     for _ in range(new_rows_count):
# #         transposed.append([])

# #     for row_idx in range(len(matrix)):
# #         for col_idx in range(len(matrix[row_idx])):
# #             transposed[col_idx].append(matrix[row_idx][col_idx])

# #     return transposed

    
# # new_matrix = transpose(matrix)

# # print(new_matrix)# == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
# # print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

# # All of these examples should print True
# print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
# print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
# print(transpose([[1]]) == [[1]])

# matrix_3_by_5 = [
#     [1, 2, 3, 4, 5],
#     [4, 3, 2, 1, 0],
#     [3, 7, 8, 6, 2],
# ]
# expected_result = [
#     [1, 4, 3],
#     [2, 3, 7],
#     [3, 2, 8],
#     [4, 1, 6],
#     [5, 0, 2],
# ]

# print(transpose(matrix_3_by_5) == expected_result)
# def rotate90(matrix):
#     new_row_count = len(matrix)
#     new_col_count = len(matrix[0])

#     transposed_matrix = [[] for i in range(new_col_count)]
    
#     for row_idx in range(new_row_count -1, -1, -1):


# matrix1 = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# matrix2 = [
#     [3, 7, 4, 2],
#     [5, 1, 0, 8],
# ]

# new_matrix1 = rotate90(matrix1)
# new_matrix2 = rotate90(matrix2)
# new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# # These examples should all print True
# print(new_matrix1)# == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
# print(new_matrix2)# == [[5, 3], [1, 7], [0, 4], [8, 2]])
# print(new_matrix3 == matrix2)

# def merge(list1, list2):
#     copy1 = list1[:]
#     copy2 = list2[:]
#     result = []

#     while copy1 and copy2:
#         if copy1[0] <= copy2[0]:
#             result.append(copy1.pop(0))
#         else:
#             result.append(copy2.pop(0))

#     return result + copy1 + copy2
    
# # # All of these examples should print True
# # print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
# # print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
# # print(merge([], [1, 4, 5]) == [1, 4, 5])
# # print(merge([1, 4, 5], []) == [1, 4, 5])

# # names1 = ['Alice', 'Kim', 'Pete', 'Sue']
# # names2 = ['Bonnie', 'Rachel', 'Tyler']
# # names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
# #                   'Rachel', 'Sue', 'Tyler']
# # print(merge(names1, names2) == names_expected)

# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst
    
#     left = merge_sort(lst[:len(lst) // 2])
#     right = merge_sort(lst[len(lst) // 2:])

#     return merge(left, right)  # Merge the sorted halves

# # All of these examples should print True
# print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
# print(merge_sort([5, 3]) == [3, 5])
# print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
# print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

# original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#             'Kim', 'Bonnie']
# expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
#             'Sue', 'Tyler']
# print(merge_sort(original) == expected)

# original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
#             43, 5, 25, 35, 18, 46]
# expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
#             35, 37, 43, 46, 51, 54]
# print(merge_sort(original) == expected)

# '''
# input: sorted list
# output: integer representing the index location (-1 if not found)

# explicit: 
#     list will be pre-sorted
#     all elements are the same type
#     the search may not contain the elementr (-1) result

# data structure: slicing the list and sublists (recursion)

# alg. 

# 1. define a function 
# 2. find center point and test against sought value
#     if center < value, recurse through rightside of list
#     if center > value, recurse through left part of list
#     recursion repeats process unitl value == centerpoint
# 3. ..? how to get the index of the value though without using .index (which is the slow method)
#     could store the discard value... so if rigth side is discarded, 
#     dont change the stored value since were still looking at the begining
#     if we discard the left side, update the stored value to the length of the section discarded
#     [0, 1, 2, 3, 4, 5, 6,] (looking for 5) center point is 3 so we discard the length of the left slice (4)
#     stored value is 4, [4, 5, 6] center is 5 stop. index is 1 from the second slice + 4 = 5

#     another example [0, 1, 2, 3, 4, ,5, 6, 7] when center is 2, we take floor so 3 and 4 means 3 is center, store 4
#     now take [4, 5, 6, 7] 
# '''
# def binary_search(lst, search):
#     def splitter(split_list):
#         return len(split_list) // 2

#     search_list = lst
#     stored_index = 0
#     while len(search_list) >= 1 and search_list[splitter(search_list)] != search:
#         if len(search_list) == 1 and search_list[0] != search:
#             return -1
#         if search_list[splitter(search_list)] > search:
#             search_list = search_list[:splitter(search_list)]
#         else: 
#             stored_index += splitter(search_list)
#             search_list = search_list[splitter(search_list):]
    
#     return splitter(search_list) + stored_index        

# # All of these examples should print True
# businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
#               'Donuts R Us', 'Eat a Lot', 'Good Food',
#               'Pasta Place', 'Pizzeria', 'Tiki Lounge',
#               'Zooper']
# print(binary_search(businesses, 'Pizzeria') == 7)
# print(binary_search(businesses, 'Apple Store') == 0)

# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

# names = []
# print(binary_search(names, 'Peter') == -1)
# print(binary_search(names, 'Tyler') == 6)
# print(binary_search(names, 'Tyler') == 6)

'''
function 1:

    input: any rational number (numerator, denominator)
    output: a list of the denominators that are part of an egyptian fraction representation of the number 
'''