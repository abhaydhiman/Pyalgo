def my_func(arr):
    max_ele = arr[-1]
    yield max_ele
    
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > max_ele:
            yield arr[i]
            max_ele = arr[i]


# driver code
ls = [16, 17, 4, 3, 5, 2]

for i in my_func(ls):
    print(i, end=' ')
