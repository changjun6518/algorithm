n = 1260
count =0

coins = [500, 100, 50, 10]

for coin in coins:
    count += n//coin
    n %= coin

print(count)


# 시간 복잡도  => 화폐 종류 K 일때 O(K)



