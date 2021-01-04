# time complexity --> O(n), space --> O(1)

def my_func(arr):
    length = len(arr)
    ptr = 0
    max_diff = 0
    start = 0
    min_ele = arr[0]
    
    while ptr < length:
        diff = arr[ptr] - arr[start]
        
        if diff > max_diff:
            max_diff = diff
        
        if (start+1) < ptr and arr[start + 1] < min_ele:
            start = start + 1
            min_ele = arr[start + 1]
        ptr += 1
    
    return max_diff


ls = [7, 9, 5, 6, 3, 2]
print(my_func(ls))
