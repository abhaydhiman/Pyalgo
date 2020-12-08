# Solution 1st (linear search)
def my_func(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1

# driver code
ls = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
print(my_func(ls))


# Solution 2nd  (binary search)        (only work if fixed point is always present in an array)
def bin_search(arr, low, high):
    mid = 0
    if high >= low:
        mid = (low + high) // 2
    
    if mid is arr[mid]:
        return mid
    
    if mid > arr[mid]:
        return bin_search(arr, (mid + 1), high)
    else:
        return bin_search(arr, low, (mid - 1))



# func calling
print(bin_search(ls, 0, len(ls)-1))