def my_func(arr):
    length = len(arr)
    row_len = length
    col_len = len(arr[0])
    
    r = 0
    c = 0
    
    while r < row_len and c < col_len:
        
        for i in range(c, col_len):
            print(arr[r][i], end=' ')
        
        r += 1
        
        for i in range(r, row_len):
            print(arr[i][col_len - 1], end=' ')
        
        col_len -= 1
        
        if r < row_len:
            for i in range(col_len - 1, c - 1, -1):
                print(arr[row_len - 1][i], end=' ')
            
            row_len -= 1
        
        if c < col_len:
            for i in range(row_len - 1, r - 1, -1):
                print(arr[i][c], end=' ')
            
            c += 1


ls = [[1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
]

my_func(ls)
