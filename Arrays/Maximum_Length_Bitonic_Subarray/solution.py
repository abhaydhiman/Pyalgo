def my_func(arr):
    length = len(arr)
    
    inc_ls = [0] * length
    
    dec_ls = [0] * length
    
    inc_ls[0] = 1
    
    dec_ls[length - 1] = 1
    
    for i in range(length):
        # print(inc_ls)
        if arr[i] >= arr[i - 1]:
            inc_ls[i] = inc_ls[i - 1] + 1
        else:
            inc_ls[i] = 1
    
    for i in range(length - 2, -1, -1):
        if arr[i] >= arr[i + 1]:
            dec_ls[i] = dec_ls[i + 1] + 1
        else:
            dec_ls[i] = 1
    
    max_num = inc_ls[0] + dec_ls[0] - 1
    
    for i in range(length):
        if inc_ls[i] + dec_ls[i] - 1 > max_num:
            max_num = inc_ls[i] + dec_ls[i] - 1
    
    return inc_ls, dec_ls, max_num


ls = [12, 4, 78, 90, 45, 23, 12]
# ls1 = [20, 4, 1, 2, 3, 4, 2, 10]
print(my_func(ls))
# print(my_func(ls1))

def my_func_2(arr):
    length = len(arr)
    counter = 1
    count = 0
    start = 0
    nextstart = 0
    
    while count < (length - 1):
        
        while (count < length - 1) and (arr[count] <= arr[count + 1]):
            count += 1
        
        while (count < length - 1) and (arr[count] >= arr[count + 1]):
            if (count < length - 1) and (arr[count] > arr[count + 1]):
                nextstart = count + 1
            count += 1
        
        counter = max(counter, count - (start - 1))
        start = nextstart
    
    return counter


print(my_func_2(ls))
