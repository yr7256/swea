T = int(input())
for t in range(T):
    N = int(input())
    coin = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    for i in coin.keys():
        coin[i] += N // i
        N %= i
    print(f'#{t+1}')
    print(*coin.values())
