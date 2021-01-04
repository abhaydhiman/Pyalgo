# O(n) in time
def my_func(arr):
    length = len(arr)
    start = 0
    end = length - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr


ls = [1, 2, 3]
print(my_func(ls))
