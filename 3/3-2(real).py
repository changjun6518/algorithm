n, m, k = map(int, input().split())
data = list(map(int, input().split()))

result = 0

data.sort()

first = data[n-1]
second = data[n-2]

count = int(m/(k+1))

rest = m%(k+1)

result = k * count * first + rest*first + second*count

print(result)