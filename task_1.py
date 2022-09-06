def get_aspected_index(two_pair_values, target_value):

    for i in two_pair_values:
        if sum(i) == target_value:
            INDEX = two_pair_values.index(i)
        
    
    return INDEX
    


two_pair_values = [
[1, 5],
[9, -7],
[0, 8],
[6, 3],
[4, 11],
[14, 0],
[8, 1],
[4, 9],
]
target_value = 9
result = get_aspected_index(two_pair_values, target_value)
print(result)
