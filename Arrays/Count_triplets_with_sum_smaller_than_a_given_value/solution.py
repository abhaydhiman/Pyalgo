def my_func(arr, sum):
    length = len(arr)
    
    # step 1st sorting
    arr.sort()
    count = 0
    
    for i in range(length):
        res = sum - arr[i]
        start = i + 1
        end = length - 1
        
        while start < end:
            if arr[start] + arr[end] < res:
                count += (end - start)
                start += 1
            else:
                end -= 1
    
    return count


ls = [5, 1, 3, 4, 7]
sum = 12
print(my_func(ls, sum))
