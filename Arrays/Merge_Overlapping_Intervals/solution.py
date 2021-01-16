# Time complexity depends upon the sorting algorithm and space is of O(1).
def my_func(arr):
    length = len(arr)
    end = length - 1
    
    # sorting based on the second number of sublist.
    arr.sort(key = lambda x: x[1])
    
    while end > 0:      # O(n)
        ls = arr[end]
        ls2 = arr[end - 1]
        
        ls_a, ls_b = ls[0], ls[1]
        ls2_a, ls2_b = ls2[0], ls2[1]
        
        if ls_a <= ls2_b <= ls_b:
            b = ls_b
        else:
            b = None
        
        if ls2_a < ls_b:
            if ls2_a <= ls_a:
                a = ls2_a
            else:
                a = ls_a
        
        else:
            a = None
        
        if a and b:
            arr[end - 1] = [a, b]
            arr[end] = 0
        
        end -= 1


ls = [[1, 3], [2, 4], [4, 8], [6, 9]]
ls1 = [[1, 3], [2, 4], [5, 7], [6, 8]]
ls2 = [[1, 9], [6, 8], [2, 4], [4, 7]]

my_func(ls2)

for i in ls2:
    if i != 0:
        print(i, end=' ')
