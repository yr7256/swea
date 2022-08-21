T = int(input())
for t in range(T):
    N = int(input())
    tri = [[0]*N for _ in range(N)]
    for i in range(N):
        tri[i][0] = tri[i][i] = 1
        for j in range(1, i):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
    print(f'#{t+1}')
    for tr in tri:
        ans = [i for i in tr if i]
        print(*ans)
