def my_func(arr):
    length = len(arr)
    
    ele = 0
    count = 1
    start = 0
    
    while count < length:
            
        if arr[ele] <= arr[count]:
            start += 1
            ele = count
            if count + 1 == length:
                print('Starting--->', ele - start, '\t\tEnding--->', ele)
        
        else:
            if ele != (ele - start):
                print('Starting--->', ele - start, '\t\tEnding--->', ele)
                start = 0
            ele = count
        
        count += 1


ls = [100, 180, 260, 310, 40, 535, 695, 200, 250, 350, 500, 700, 750]
my_func(ls)
