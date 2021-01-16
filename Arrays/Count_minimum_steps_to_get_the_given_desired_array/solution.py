def my_func(arr):
    length = len(arr)
    step = 0
    
    while True:
        checker = True
        
        if arr.count(0) == length:
            break
        
        for i in range(length):
            if arr[i] % 2 != 0:
                arr[i] -= 1
                step += 1
                checker = False
        
        if checker:
            for i in range(length):
                arr[i] = arr[i] // 2
            step += 1
    
    return step


ls = [16, 16, 16]
print(my_func(ls))
