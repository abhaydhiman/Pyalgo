# time complexity depends upon the soting
def my_func(arr):
    # step - 1st ------ sorting
    arr.sort()
    
    # step 2nd main logic
    start = 0
    end = len(arr) - 1
    
    diff = 10**20
    min_ele = 0
    max_ele = len(arr) - 1
    
    while start < end:
        summation = arr[start] + arr[end]
        
        if summation == 0:
            return f"elements are ({arr[start]}, {arr[end]})"
        
        elif summation < 0:
            summ = abs(summation)
            if summ < diff:
                diff = summ
                min_ele = arr[start]
                max_ele = arr[end]
            
            start += 1
        
        else:
            summ = abs(summation)
            if summ < diff:
                diff = summ
                min_ele = arr[start]
                max_ele = arr[end]
            
            end -= 1
    
    return f"elements are ({min_ele}, {max_ele})"


# driver code
ls = [1, 60, -10, 70, -80, 85]
print(my_func(ls))
