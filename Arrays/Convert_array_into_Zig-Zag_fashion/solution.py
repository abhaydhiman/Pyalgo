def my_func(arr):
    length = len(arr)
    
    count = 0
    flag = True
    
    while count < length - 1:
        if arr[count] > arr[count + 1]:
            if flag == True:
                arr[count], arr[count + 1] = arr[count + 1], arr[count]
                flag = False
            else:
                flag = True
        
        elif arr[count] < arr[count + 1]:
            if flag == False:
                arr[count], arr[count + 1] = arr[count + 1], arr[count]
                flag = True
            else:
                flag = False
        
        count += 1
    
    return arr


ls = [4, 3, 7, 8, 6, 2, 1]
print(my_func(ls))
