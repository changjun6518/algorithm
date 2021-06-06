
arr = []

N, M = map(int,input().split(" "))

for i in range(N):
    arr.append(list(map(int, input())))



def dfs(arr, i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return False
    if arr[i][j] == 0:
        arr[i][j] = 1
        dfs(arr,i-1,j)
        dfs(arr,i,j-1)
        dfs(arr,i+1,j)
        dfs(arr,i,j+1)
        return True
    return False

result = 0

for i in range(N):
    for j in range(M):
        if dfs(arr,i,j) == True:
            result += 1

print(result)
