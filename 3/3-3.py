import numpy as np

a, b = map(int, input().split())


arr = []
for i in range(0,a):
    row = list(map(int, input().split()))
    arr.append(row)

arr = np.array(arr)

max = 0
for i in range(0,a):
    min = 10000
    for j in range(0,b):
        if arr[i][j] <= min:
            min = arr[i][j]
    if min >= max:
        max = min

print(max)








