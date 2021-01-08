def my_func(arr):
    length = len(arr)
    
    # step - 1st sorting
    
    arr.sort()
    max_len = 1
    res = 0
    
    for i in range(length - 1):
        diff = arr[i + 1] - arr[i]
        
        if diff == 1:
            max_len += diff
        else:
            max_len = 1
        
        res = max(max_len, res)
    
    return res


ls = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
print(my_func(ls))
