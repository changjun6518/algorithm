from collections import deque

n,m = map(int,input().split(" "))

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [0,-1,0,1]
dy = [-1, 0, 1, 0]


def bfs(graph, x, y):

    queue = deque()

    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            else:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

                if nx == n-1 and ny == m-1:
                    return graph[n-1][m-1]


result = bfs(graph, 0, 0)
print(result)



