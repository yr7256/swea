dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(10):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    x, y = 0, 0
    ans = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                x, y = i, j
    queue = [[x, y]]
    while queue:
        x0, y0 = queue.pop()
        for d in range(4):
            x1 = x0+dx[d]
            y1 = y0+dy[d]
            if 0 <= x1 < 100 and 0 <= y1 < 100:
                if not arr[x1][y1]:
                    arr[x1][y1] = 1
                    queue.append([x1, y1])
                if arr[x1][y1] == 3:
                    ans = 1
                    queue.clear()
                    break
    print(f'#{T} {ans}')
