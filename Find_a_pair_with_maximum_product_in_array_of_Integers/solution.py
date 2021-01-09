def my_func(arr):
    length = len(arr)
    start = 0
    end = length - 1
    
    # step 1st -- sorting
    arr.sort()
    
    ans1 = arr[start] * arr[start + 1]
    ans2 = arr[end] * arr[end - 1]
    
    if ans1 > ans2:
        return (arr[start + 1], arr[start])
    else:
        return (arr[end - 1], arr[end])


ls = [-1, -3, -4, 2, 0, -5]
ls2 = [1, 4, 3, 6, 7, 0]
print(my_func(ls2))
