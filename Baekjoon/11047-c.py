n, k = map(int, input().split())
counts = 0
coin_list = []

for _ in range(n):
    coins = int(input())
    coin_list.append(coins)

coin_list.reverse()  # 큰 수부터 가도록 뒤집기

for coin in coin_list:
    if int(k / coin):
        counts += int(k / coin)
        k %= coin

print(counts)
