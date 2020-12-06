# First Step --- Sorting
ls = [1, 2, 4, 6, 3, 7, 8]
ls.sort()

# If the element is not equal to its index plus one 
# then thats the output and break from the loop then. 
for i in range(len(ls)):
    if ls[i] != (i + 1):
        print(i + 1)
        break
