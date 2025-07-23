# print('Enter 2 numbers')
# num1 = int(input())
# num2 = int(input())

# try:
#     print(f'{num1 / num2}')
# except(ZeroDivisionError):
#     print('zero error')
# except(ValueError):
#     print('value error')
# finally:
#     print('end of program')
    
# 
def inversion(lst):
    try:
        new_lst = [1 / lst[i] for i in range(len(lst))]
        return new_lst
    except Exception:
        return 'list contains an invalid number'

print(inversion([1, 2, 3, 0]))