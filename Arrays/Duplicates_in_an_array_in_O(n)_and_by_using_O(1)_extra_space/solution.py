def my_func(arr, num):
    for i in range(num):
        index = arr[i] % num             # if two elements are same then index value is same for both
        arr[index] += num
    
    for i in range(num):
        if (arr[i]/num) >= 2:            # for result; I also didn't get that properly.
            print(i, end=" ")



# driver code
ls = [1, 2, 3, 1, 3, 6, 6]
n = 7
my_func(ls, n)
