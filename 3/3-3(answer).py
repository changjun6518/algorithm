n, m = map(int, input().split())


max = 0
for i in range(n):
    data = map(int, input().split())
    min_one = min(data)
    max = max(max, min_one)

print(max)
