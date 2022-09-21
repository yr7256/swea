T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    H = [0] + list(map(int, input().split()))
    H.sort()
    sum_H = sum(H)
    dp = [[0]*(sum_H+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, sum_H+1):
            if H[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - H[i]] + H[i])
    ans = 200000
    for i in dp[N]:
        if i-B >= 0:
            ans = min(ans, i-B)
    print(f'#{t+1} {ans}')
