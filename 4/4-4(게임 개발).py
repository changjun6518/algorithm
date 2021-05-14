import numpy as np

N, M = map(int, input().split())

x, y ,direction = map(int, input().split())

dy = [0,1,0,-1]
dx = [-1,0,1,0]

d = [[0]*M for _ in range(N)]


arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny]==0 and arr[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x -dx[direction]
        ny = y -dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)



