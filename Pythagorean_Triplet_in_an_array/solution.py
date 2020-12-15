# O(n^2)---- time complexity.
def my_func(arr):
    # step 1st sorting
    arr.sort()
    
    # step 2nd squaring
    arr = [i**2 for i in arr]
    
    for i in range(len(arr)):
        x = 0
        y = len(arr) - 1
        
        while (x < y):
            if arr[x] + arr[y] == arr[i]:
                return True
            elif arr[x] + arr[y] > arr[i]:
                y -= 1
            else:
                x += 1
    return False


ls = [10, 4, 6, 12, 5]
print(my_func(ls))
