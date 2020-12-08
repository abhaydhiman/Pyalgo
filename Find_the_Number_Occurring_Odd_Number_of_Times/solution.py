# Solution number 1st:-     time complexity--> O(n), space complexlity--> O(n)
def my_func(arr):
    my_dict = dict()
    length = len(arr)
    
    for i in range(length):
        check = my_dict.get(arr[i], None)
        
        if check:
            my_dict[arr[i]] += 1
        else:
            my_dict[arr[i]] = 1
    
    for key, value in my_dict.items():
        if value % 2 != 0:
            return key


# driver code
ls = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
print(my_func(ls))


# Solution number 2nd         time complexity--> O(n),  space complexity--> O(1)

def getOddOccurrence(arr):

    # Initialize result
    res = 0

    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element

    return res


# Test array
arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]

print(getOddOccurrence(arr))
