def remove_duplicates(array):
    if len(array) == 0:
        return array
    
    unique_index = 0
    
    for i in range(1, len(array)):
        if array[i] != array[unique_index]:
            unique_index += 1
            array[unique_index] = array[i]
    
    return array[:unique_index + 1]

array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print(remove_duplicates(array1))  
print(remove_duplicates(array2))  
