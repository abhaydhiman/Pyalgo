def my_func(arr):
    length = len(arr)
    
    count = 0
    ptr = 0
    
    while ptr < length:
        if arr[ptr] == 0:
            arr.pop(ptr)
            count += 1
            length -= 1
        ptr += 1
    
    for _ in range(count):
        arr.append(0)
    
    return arr


ls = [1, 2, 0, 4, 3, 0, 5, 0]
print(my_func(ls))

def my_func2(arr):
    length = len(arr)
    
    count = 0
    
    for i in range(length):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    
    while count < length:
        arr[count] = 0
        count += 1
    
    return arr


ls = [1, 2, 0, 4, 3, 0, 5, 0]
print(my_func2(ls))
