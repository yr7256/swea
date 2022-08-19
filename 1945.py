T = int(input())
for t in range(T):
    N = int(input())
    dic = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    while True:
        if N == 1:
            break
        for i in dic:
            if N % i == 0:
                N //= i
                dic[i] += 1
    print(f'#{t+1}', end=' ')
    for i in dic.values():
        print(i, end=' ')
    print()
