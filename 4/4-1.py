import numpy as np

N = int(input())

arr = np.zeros((N+2,N+2))
arr[1:N+1,1:N+1] = 1


i= 1
j = 1
data = input().split()
for dir in data:
    if dir == "L":
        if arr[i][j] == 0:
            j += 1
        j -= 1
    elif dir == "R":
        if arr[i][j] == 0:
            j -= 1
        j += 1
    elif dir == "U":
        if arr[i][j] == 0:
            i -= 1
        i += 1
    elif dir == "D":
        if arr[i][j] == 0:
            i += 1
        i -= 1
    print("i :", i,"j : ",j)

print(arr)

print(i ,j)







