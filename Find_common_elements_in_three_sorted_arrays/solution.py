def my_func(arr1, arr2, arr3):
    ln1 = len(arr1)
    ln2 = len(arr2)
    ln3 = len(arr3)
    ptr1 = 0
    ptr2 = 0
    ptr3 = 0
    
    while ptr1 < ln1 and ptr2 < ln2 and ptr3 < ln3:
        if arr1[ptr1] < arr2[ptr2]:
            if arr3[ptr3] < arr2[ptr2]:
                arr1[ptr1] = -1
                arr3[ptr3] = -1
                ptr3 += 1
                ptr1 += 1
            else:
                arr1[ptr1] = -1
                ptr1 += 1
        
        elif arr2[ptr2] < arr3[ptr3]:
            if arr1[ptr1] < arr3[ptr3]:
                arr1[ptr1] = -1
                arr2[ptr2] = -1
                ptr1 += 1
                ptr2 += 1
            else:
                arr2[ptr2] = -1
                ptr2 += 1
        
        elif arr3[ptr3] < arr1[ptr1]:
            if arr2[ptr2] < arr1[ptr1]:
                arr2[ptr2] = -1
                arr3[ptr3] = -1
                ptr2 += 1
                ptr3 += 1
            else:
                arr3[ptr3] = -1
                ptr3 += 1
        
        else:
            ptr1 += 1
            ptr2 += 1
            ptr3 += 1
        
    for i in arr1:
        if i != -1:
            print(i, end=' ')
    

ls1 = [1, 5, 5]
ls2 = [3, 4, 5, 5, 10]
ls3 = [5, 5, 10, 20]
my_func(ls1, ls2, ls3)
