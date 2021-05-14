n = 1260
count = 0
coins = [500, 100, 50, 10]

for coin in coins:
    while(1):
        if n >= coin:
            n = n - coin
            count = count + 1
            if n < coin:
                break

print(count)



