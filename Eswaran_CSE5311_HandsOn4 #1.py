def merge_k_sorted_arrays(arrays):
    merged_list = []
    for array in arrays:
        merged_list.extend(array)
    
    merged_list.sort()
    
    return merged_list

arrays1 = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]

arrays2 = [
    [1, 3, 7],
    [2, 4, 8],
    [9, 10, 11]
]

print(merge_k_sorted_arrays(arrays1))  
print(merge_k_sorted_arrays(arrays2))  