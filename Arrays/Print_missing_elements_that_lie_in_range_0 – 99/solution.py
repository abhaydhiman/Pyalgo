def my_func(arr):
    start = 0
    
    for num in range(100):
        if num in arr:
            if (num - 1) == start:
                print(start)

            elif (num - 1) > start:
                print(f"{start} - {num - 1}")

            start = num + 1

    if num == 99:
        if start < num:
            print(f"{start} - {num}")

        elif start == num:
            print(start)


ls = [9, 6, 900, 850, 5, 90, 100, 99]
my_func(ls)
