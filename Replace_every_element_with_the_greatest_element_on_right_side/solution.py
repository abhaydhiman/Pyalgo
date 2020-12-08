def my_func(arr):
    max_ele = arr[-1]
    arr[-1] = -1
    length = len(arr)
    
    for i in range(length - 2, -1, -1):
        
        temp = arr[i]
        arr[i] = max_ele
        if temp > max_ele:
            max_ele = temp


# driver code
ls = [16, 17, 4, 3, 5, 2]
my_func(ls)
print(ls)