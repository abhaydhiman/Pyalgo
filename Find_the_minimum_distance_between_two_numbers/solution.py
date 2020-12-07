arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
X = 3
Y = 6

min_distance = len(arr)
prev = 0

for i in range(len(arr)):
    if X == arr[i] or Y == arr[i]:
        prev = i
        break

for i in range(prev, len(arr)):
    if arr[i] == X or arr[i] == Y:
        if arr[prev] != arr[i]:
            min_distance = min(min_distance, i-prev)
        else:
            prev = i

print(min_distance)
