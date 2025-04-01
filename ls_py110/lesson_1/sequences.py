'''
1. create an empty dictionary
2. add key, value pair - key is the row, value is the last row's vlaue + the square of the current key
3. repeat step 2 until the NEXT pair to be added exceeds the input integer
4. subract the last created value from the input integer
5. return the difference (blocks remaining)
'''

def builder(avail_blocks):
    structure_rows = {0 : 0}
    prev_layer = 0
    current_layer = 1
    
    while avail_blocks >= structure_rows[prev_layer]:
        
        structure_rows[current_layer] = (prev_layer + current_layer*2)
        current_layer += 1
        prev_layer += 1
        
        
    return int(avail_blocks) - structure_rows[current_layer]


print(builder(10))

