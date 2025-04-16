def join_or(numbers, delimiter=',', conjunction='or'):
    lst = [str(i) for i in numbers]
    
    if len(lst) == 0:
        return ''
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return f'{lst[0]} {conjunction} {lst[1]}'
    
    return f"{delimiter} ".join(lst[:-1]) + f'{delimiter} {conjunction} {lst[-1]}'

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], ';'))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ',', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"