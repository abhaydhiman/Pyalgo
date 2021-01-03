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
    
    
    # length = len(arr)
    # start = 0
    # end = length - 1
    # ls = []
    
    # while start < end:
    #     if arr[start] > arr[start + 1]:
    #         start += 1
        
    #     elif arr[end] > arr[end - 1]:
    #         end -= 1
        
    #     print(arr[start])
    #     print(arr[end])
    #     if arr[start] < arr[start+1] and arr[end] < arr[end - 1]:
    #         ls.append(arr[start])
    #         ls.append(arr[end])
    #         start += 1
    #         end -= 1
    
    # return ls


ls = [12, 4, 78, 90, 45, 23, 12]
# ls1 = [20, 4, 1, 2, 3, 4, 2, 10]
print(my_func(ls))
# print(my_func(ls1))
