T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    target = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    ans = 0
    if N <= M:
        for i in range(M-N+1):
            temp = 0
            for j in range(N):
                temp += target[j]*lst[i+j]
            ans = max(ans, temp)
        print(f'#{t+1} {ans}')
    else:
        for i in range(N - M + 1):
            temp = 0
            for j in range(M):
                temp += target[i+j] * lst[j]
            ans = max(ans, temp)
        print(f'#{t + 1} {ans}')
