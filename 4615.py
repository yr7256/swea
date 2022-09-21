dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2] = 2
    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    for _ in range(M):
        x, y, stone = map(int, input().split())
        x -= 1
        y -= 1
        if not arr[x][y]:
            arr[x][y] = stone
            for i in range(8):
                x1 = x + dx[i]
                y1 = y + dy[i]
                change = []
                while True:
                    if 0 <= x1 < N and 0 <= y1 < N:
                        if arr[x1][y1] == stone:
                            break
                        if not arr[x1][y1]:
                            change = []
                            break
                        else:
                            change.append([x1, y1])
                            x1 += dx[i]
                            y1 += dy[i]
                    else:
                        change = []
                        break
                for a, b in change:
                    arr[a][b] = stone
    B, W = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                B += 1
            if arr[i][j] == 2:
                W += 1
    print(f'#{t+1} {B} {W}')