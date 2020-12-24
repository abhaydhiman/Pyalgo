# Ceiling ------ bin search O(logn)
def ceiling(arr, start, end, x):
    if x <= arr[start]:
        return arr[start]
    if x > arr[end]:
        return -1
    
    mid = (start + end) // 2
    
    if arr[mid] == x:
        return arr[mid]
    
    elif x > arr[mid]:
        if arr[mid + 1] >= x and (mid + 1) <= end:
            return arr[mid + 1]
        return ceiling(arr, mid + 1, end, x)
    
    else:
        if x > arr[mid - 1] and (mid - 1) >= start:
            return arr[mid]
        return ceiling(arr, start, mid - 1, x)


# floar
def floaring(arr, start, end, x):
    if x >= arr[end]:
        return arr[end]
    if x < arr[start]:
        return -1
    
    mid = (start + end) // 2
    
    if x == arr[mid]:
        return arr[mid]

    elif x > arr[mid]:
        if arr[mid + 1] > x and (mid + 1) <= end:
            return arr[mid]
        return floaring(arr, mid + 1, end, x)

    else:
        if arr[mid - 1] <= x and (mid - 1) >= start:
            return arr[mid - 1]
        return floaring(arr, start, mid - 1, x)


ls = [1, 2, 8, 10, 10, 12, 19]
x = 9
end = len(ls) - 1
print("ceil value --> ", ceiling(ls, 0, end, x))
print("floar value --> ", floaring(ls, 0, end, x))
