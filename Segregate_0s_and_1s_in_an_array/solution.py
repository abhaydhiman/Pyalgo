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

# Solution number 2nd

def func_number_second(arr):
    length = len(arr)
    counter_1 = arr.count(1)
    counter_0 = length - counter_1
    
    ls = [0]*(counter_0) + [1]*(counter_1)
    
    return ls

print(func_number_second(ls))
