def my_func(arr):
    length = len(arr)
    
    start = 0
    end = length - 1
    count = 0
    
    while start < end:
        if arr[start] != arr[end]:
            res = arr[start] + arr[end]
            arr[start], arr[end] = res, res
            count += 1
        start += 1
        end -= 1
        print(arr)
    return count


ls = [1, 4, 5, 9, 1]
print(my_func(ls))
