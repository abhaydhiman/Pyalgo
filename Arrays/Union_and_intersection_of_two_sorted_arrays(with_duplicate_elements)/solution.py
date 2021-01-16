''' First solution of this problem is to pass the arrays
by removing the duplicates from them(using sets available in python)
then previous method will work perfectly.

Solution 2nd:- see `duplicate_remover` function thats the only change
in the previous code.
'''


class Solution:
    def __init__(self, arr1, arr2) -> None:
        self.arr1 = arr1
        self.arr2 = arr2
        self.ln1 = len(arr1)
        self.ln2 = len(arr2)
    
    @staticmethod
    def duplicate_remover(ls, arr, indexer, z):
        if z != 0:
            if arr[indexer] != ls[-1]:
                ls.append(arr[indexer])
        else:
            ls.append(arr[indexer])
    
    def union(self):
        
        i = 0
        j = 0
        z = 0       # pivot for union_ls
        union_ls = []
        
        while i < self.ln1 and j < self.ln2:
            if self.arr1[i] > self.arr2[j]:
                self.duplicate_remover(union_ls, self.arr2, j, z)
                j += 1
                z += 1
            
            elif self.arr1[i] < self.arr2[j]:
                self.duplicate_remover(union_ls, self.arr1, i, z)
                i += 1
                z += 1
            
            else:
                self.duplicate_remover(union_ls, self.arr1, i, z)
                i += 1
                j += 1
                z += 1
        
        while i < self.ln1:
            self.duplicate_remover(union_ls, self.arr1, i, z)
            i += 1
            z += 1
        
        while j < self.ln2:
            self.duplicate_remover(union_ls, self.arr2, j, z)
            j += 1
            z += 1
        
        return union_ls
    
    def intersection(self):
        
        i = 0
        j = 0
        z = 0       # pivot for intersection_ls
        intersec_ls = []
        
        while i < self.ln1 and j < self.ln2:
            if self.arr1[i] > self.arr2[j]:
                j += 1
            
            elif self.arr1[i] < self.arr2[j]:
                i += 1
            
            else:
                self.duplicate_remover(intersec_ls, self.arr1, i, z)
                i += 1
                j += 1
                z += 1
        
        return intersec_ls


# Driver program
ls1 = [1, 2, 4, 4, 5, 5, 6]
ls2 = [2, 3, 4, 4, 5, 7]
obj = Solution(arr1=ls1, arr2=ls2)

print(' Union of the two arrays--> ', obj.union())
print('-'*50)
print('Intersection of the two arrays', obj.intersection())
