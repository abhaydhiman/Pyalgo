def my_func(arr1, arr2):
    for ele in arr1:
        if ele not in arr2:
            return ele
        else:
            arr2.remove(ele)
    
    return arr2[0]


# driver code
ls1 = [2, 3, 4, 5]
ls2 = [2, 3, 4, 5, 6]

print(my_func(ls1, ls2))
