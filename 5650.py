from collections import defaultdict


def pinball(x, y, d):
    global ans
    x0, y0 = x, y
    count = 0
    while True:
        x += dx[d]
        y += dy[d]
        if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] == 5:
            count += 1
            d = (d+2) % 4
        elif arr[x][y] == -1 or (x, y) == (x0, y0):
            break
        elif arr[x][y] in range(6, 11):
            for h in hole[arr[x][y]]:
                if h != (x, y):
                    x, y = h
                    break
            # x, y = teleport[(x, y)][0], teleport[(x, y)][1]
        elif arr[x][y] == 1:
            count += 1
            if d == 1:
                d = 0
            if d == 2:
                d = 3
            else:
                d = (d+2) % 4
        elif arr[x][y] == 2:
            count += 1
            if d == 0:
                d = 3
            if d == 1:
                d = 2
            else:
                d = (d+2) % 4
                # break
        elif arr[x][y] == 3:
            count += 1
            if d == 0:
                d = 1
            if d == 3:
                d = 2
            else:
                d = (d+2) % 4
                # break
        elif arr[x][y] == 4:
            count += 1
            if d == 3:
                d = 0
            if d == 2:
                d = 1
            else:
                d = (d+2) % 4
                # break
    ans = max(ans, count)


dx = [-1, 0, 1, 0]  # 상 좌 하 우
dy = [0, -1, 0, 1]
T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hole = defaultdict(list)
    # queue = set()
    for i in range(N):
        for j in range(N):
            # if not arr[i][j]:
            #     queue.add((i, j))
            if arr[i][j] in range(6, 11):
                hole[arr[i][j]].append((i, j))
    # teleport = {}
    # for i in hole:
    #     teleport[hole[i][0]] = hole[i][1]
    #     teleport[hole[i][1]] = hole[i][0]
    ans = 0
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                for k in range(4):
                    pinball(i, j, k)
    print(ans)

