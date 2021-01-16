# Solution number 1st:-          time complexity--> unclear!!
def my_func(arr):
    length = len(arr)// 2
    
    for i in range(len(arr)):
        value = arr.count(arr[i])
        if value > length:
            return arr[i]
    return "No Majority Element"


# driver code
ls = [3, 3, 4, 2, 4, 4, 2, 4, 4]

print(my_func(ls))

# Solution number 2nd:-           time complexity--> O(n)
def my_func_2(arr):
    my_dict = dict()
    length = len(arr) // 2
    
    for i in range(len(arr)):
        check = my_dict.get(arr[i], None)
        if check:
            my_dict[arr[i]] += 1
        else:
            my_dict[arr[i]] = 1
        
        value = my_dict[arr[i]]
        if value  > length:
            return arr[i]
    return "No Majority Element"

print(my_func_2(ls))
