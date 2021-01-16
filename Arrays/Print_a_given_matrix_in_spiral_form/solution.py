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


# class DFS:
#     def __init__(self, arr):
#         self.arr = arr
#         self.R = len(arr[0]) - 1
#         self.C = len(arr) - 1
    
#     def is_in_bound(self, i, j):
#         if i < 0 or i >= self.R or j < 0 or j>=self.C:
#             return False
#         return True
    
#     def is_blocked(self, i, j):
#         print('-'*50)
#         print(i, j)
#         print('-'*50)
        
#         if not self.is_in_bound(i, j):
#             return True
        
#         elif self.arr[i][j] == -1:
#             return True
#         return False
    
#     def spirally_DFS(self, i, j, dir, res):
#         if self.is_blocked(i, j):
#             return
#         print('hi')
#         all_blocked = True
        
#         for k in range(-1, 2, 2):
#             all_blocked = all_blocked and self.is_blocked( k + i, j) \
#                 and self.is_blocked(i, j + k)
        
#         res.add(self.arr[i][j])
#         self.arr[i][j] = -1
        
#         if all_blocked:
#             return
        
#         nxt_i = i
#         nxt_j = j
#         nxt_dir = dir
        
#         if dir == 0:
#             if not self.is_blocked(i, j + 1):
#                 nxt_j += 1
#             else:
#                 nxt_dir = 1
#                 nxt_i += 1
#         elif dir == 1:
#             if not self.is_blocked(i + 1, j):
#                 nxt_i += 1
#             else:
#                 nxt_dir = 2
#                 nxt_j -= 1
#         elif dir == 2:
#             if not self.is_blocked(i, j - 1):
#                 nxt_j -= 1
#             else:
#                 nxt_dir = 3
#                 nxt_i -= 1
#         elif dir == 3:
#             if not self.is_blocked(i - 1, j):
#                 nxt_i -= 1
#             else:
#                 nxt_dir = 0
#                 nxt_j += 1
        
#         return self.spirally_DFS(nxt_i, nxt_j, nxt_dir, res)


# store = set()

# obj = DFS(ls)
# obj.spirally_DFS(0, 0, 0, store)
# print(store)
