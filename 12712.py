dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ddx = [1, 1, -1, -1]
ddy = [1, -1, 1, -1]
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            temp1 = arr[i][j]
            temp2 = arr[i][j]
            for k in range(1, M):
                for l in range(4):
                    x1 = i + dx[l]*k
                    y1 = j + dy[l]*k
                    x2 = i + ddx[l]*k
                    y2 = j + ddy[l]*k
                    if 0 <= x1 < N and 0 <= y1 < N:
                        temp1 += arr[x1][y1]
                    if 0 <= x2 < N and 0 <= y2 < N:
                        temp2 += arr[x2][y2]
            ans = max(ans, temp1, temp2)
    print(f'#{t+1} {ans}')