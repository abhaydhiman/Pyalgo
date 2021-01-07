arr = [2, 5, 3, 5, 4, 4, 2, 1, 3, 3, 2]
X = 2
Y = 3

min_distance = len(arr)
prev = 0

for i in range(len(arr)):
    if X == arr[i] or Y == arr[i]:
        prev = i
        break

for i in range(prev+1, len(arr)):
    if arr[i] == X or arr[i] == Y:
        if arr[prev] != arr[i]:
            min_distance = min(min_distance, i-prev)
            prev = i
        else:
            prev = i

print(min_distance)
