# Complexity depend upon sorting algo.
def my_func(arr):
    # step 1st --- sorting
    arr.sort()
    
    min_dist = 10**20
    
    # main logic
    for index in range(len(arr)-1):
        diff = arr[index + 1] - arr[index]
        
        if diff < min_dist:
            min_dist = diff
    
    return min_dist


# driver code
ls = [1, 5, 3, 19, 18, 25]
print(my_func(ls))
