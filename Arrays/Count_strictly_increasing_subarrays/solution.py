def my_func(arr):
    count = 0
    length = 1
    
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            length += 1
        
        else:
            count += (length*(length - 1)) // 2
            length = 1
    
    # if counter not goes on else condition but we have to check for the length also:-
    if length > 1:
        count += (length * (length - 1)) // 2
    
    return count

ls = [1, 2, 3, 4]
print(my_func(ls))
