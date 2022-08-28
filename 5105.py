"""
dx dy로 방향값 정해주고 처음 x,y 값을 찾는다. 그리고 queue에 처음 x,y 값을 넣고 뽑기
"""
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j
    queue = [[x, y]]
    ans = 0
    while queue:
        x0, y0 = queue.pop(0)
        for i in range(4):                                      # 4방향 탐색하기
            x1 = x0 + dx[i]
            y1 = y0 + dy[i]
            temp = 0
            if 0 <= x1 < N and 0 <= y1 < N:
                if not arr[x1][y1] and not visited[x1][y1]:
                    visited[x1][y1] = visited[x0][y0] + 1
                    queue.append([x1, y1])
                if arr[x1][y1] == 3:
                    visited[x1][y1] = visited[x0][y0]
                    ans = visited[x1][y1]
                    queue.clear()
                    break
    print(f'#{t+1} {ans}')
