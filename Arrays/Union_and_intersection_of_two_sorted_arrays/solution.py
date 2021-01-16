class Solution:
    def __init__(self, arr1, arr2) -> None:
        self.arr1 = arr1
        self.arr2 = arr2
        self.ln1 = len(arr1)
        self.ln2 = len(arr2)
    
    def union(self):
        
        i = 0
        j = 0
        union_ls = []
        
        while i < self.ln1 and j < self.ln2:
            if self.arr1[i] > self.arr2[j]:
                union_ls.append(self.arr2[j])
                j += 1
            
            elif self.arr1[i] < self.arr2[j]:
                union_ls.append(self.arr1[i])
                i += 1
            
            else:
                union_ls.append(self.arr1[i])
                i += 1
                j += 1
        
        while i < self.ln1:
            union_ls.append(self.arr1[i])
            i += 1
        
        while j < self.ln2:
            union_ls.append(self.arr2[j])
            j += 1
        
        return union_ls
    
    def intersection(self):
        
        i = 0
        j = 0
        intersec_ls = []
        
        while i < self.ln1 and j < self.ln2:
            if self.arr1[i] > self.arr2[j]:
                j += 1
            
            elif self.arr1[i] < self.arr2[j]:
                i += 1
            
            else:
                intersec_ls.append(self.arr1[i])
                i += 1
                j += 1
        
        return intersec_ls


# Driver program
ls1 = [1, 2, 4, 5, 6]
ls2 = [2, 3, 5, 7]
obj = Solution(arr1 = ls1, arr2 = ls2)

print(' Union of the two arrays--> ', obj.union())
print('-'*50)
print('Intersection of the two arrays', obj.intersection())


'''
Q1- What if i have to find the union and intersection of more then two
arrays?
Q2- What if there are duplicate elements present in my array?
'''
