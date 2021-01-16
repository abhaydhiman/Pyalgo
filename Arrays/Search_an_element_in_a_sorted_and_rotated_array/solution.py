def my_func(arr, start, end, key):
    if start > end:
        return 'Not Found'
    
    mid = (start + end) // 2
    
    if key == arr[mid]:
        return mid
    
    elif arr[start] < arr[mid]:
        if key < arr[mid] and key >= arr[start]:
            return my_func(arr, start, mid - 1, key)
        return my_func(arr, mid + 1, end, key)
    
    elif arr[end] > arr[mid]:
        if key > arr[mid] and key <= arr[end]:
            return my_func(arr, mid + 1, end, key)
        return my_func(arr, start, mid - 1, key)
    
    else:
        return 'Not Found'


ls = [5, 6, 7, 8, 9, 10, 1, 2, 3]
l = 0
r = len(ls) - 1

for key in range(11):
    print(my_func(ls, l, r, key))
