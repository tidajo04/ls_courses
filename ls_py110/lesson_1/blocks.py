'''
1. create an empty dictionary
2. add key, value pair - key is the row, value is the last row's vlaue + the square of the current key
3. repeat step 2 until the NEXT pair to be added exceeds the input integer
4. subract the last created value from the input integer
5. return the difference (blocks remaining)
'''

def calculate_leftover_blocks(avail_blocks):
    structure_rows = {0 : 0}
    prev_layer = 0
    current_layer = 1
    
    while avail_blocks >= structure_rows[prev_layer]:
        structure_rows[current_layer] = (structure_rows[prev_layer] + current_layer ** 2)
        current_layer += 1
        prev_layer += 1    
        
    return avail_blocks - structure_rows[prev_layer - 1]


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True


