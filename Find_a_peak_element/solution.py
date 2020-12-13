# Simple approach :- O(n)
def my_func(arr):
    length = len(arr)
    
    if length == 1:
        return 0
    elif arr[0] > arr[1]:
        return 0
    elif arr[-1] > arr[-2]:
        return length - 1
    else:
        for i in range(1, length-1):
            if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                return i


ls = [1, 3, 20, 4, 1, 0]
print(my_func(ls))

# 2nd Approach :- O(logn); similar to binary search or particularly its `divide and conquer`.

def find_index(arr, length, start, end):
    mid = (start + end) //2
    
    if mid == 0 or mid == (length-1):
        return mid
    elif arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return mid
    elif (mid < (length - 1)) and arr[mid + 1] > arr[mid]:
        return find_index(arr, length, (mid+1), end)
    else:
        return find_index(arr, length, start, (mid - 1))
    

length = len(ls)
start = 0
end = length - 1
print(find_index(ls, length, start, end))
