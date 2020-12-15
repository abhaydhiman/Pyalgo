# O(n) --- time complexity.
def my_func(arr):
    start= 0
    end = len(arr) - 1
    
    while start < end:
        if arr[start] == 0:
            start += 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1
    
    return arr


ls = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(my_func(ls))
