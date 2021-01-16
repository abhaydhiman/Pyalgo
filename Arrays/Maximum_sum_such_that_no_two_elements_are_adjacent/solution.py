def my_func(arr):
    length = len(arr)
    pos1 = 0
    pos2 = 1
    
    res1 = 0
    res2 = 0
    
    while pos1 < length:
        res1 += arr[pos1]
        pos1 += 2
    
    while pos2 < length:
        res2 += arr[pos2]
        pos2 += 2
    
    return max(res1, res2)


ls = [5, 5, 10, 100, 10, 5]
print(my_func(ls))
