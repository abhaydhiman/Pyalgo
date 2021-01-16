# Solution 1st
def my_func(arr, num):
    # Step 1 --- sorting
    arr.sort()
    
    # Step 2 --- main logic using two pointers/variables.
    start = 0
    end = len(arr) - 1
    
    while start < end:
        summation = arr[start] + arr[end]
        if summation < num:
            start += 1
        elif summation > num:
            end -= 1
        else:
            return f"Pair exist; ({arr[start]}, {arr[end]})"
    return "No Pair exist"


# driver code
ls = [1, 4, 45, 6, 10, -8]
n = 16
print(my_func(ls, n))

# Solution 2nd
def funcname(arr, num):
    ls = []
    
    for arr_num in arr:
        res = num - arr_num
        if res in ls:
            return f"Pair exist; ({arr_num}, {res})"
        else:
            ls.append(arr_num)
    return "No pair exist"


# driver code
print(funcname(ls, n))