def func(arr, k):
    length = len(arr)
    element = arr[0]
    
    for i in range(length):
        for j in range(i, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        if (k - 1) == i:
            print(arr[i])
            break


# --------------
arr = [7, 10, 4, 3, 20, 15]
k = 3
func(arr, k)
