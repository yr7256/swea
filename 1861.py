from collections import deque


def bfs(x, y):
    queue = deque([[x, y]])
    count = 1
    while queue:
        x0, y0 = queue.popleft()
        for i in range(4):
            x1 = x0 + dx[i]
            y1 = y0 + dy[i]
            if 0 <= x1 < N and 0 <= y1 < N:
                if arr[x1][y1] - arr[x0][y0] == 1:
                    queue.append([x1, y1])
                    count += 1
    return count


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_room_num = 1000000
    max_visited = 0
    for i in range(N):
        for j in range(N):
            max_visited = max(max_visited, bfs(i, j))
    for i in range(N):
        for j in range(N):
            if bfs(i, j) == max_visited:
                min_room_num = min(min_room_num, arr[i][j])
    print(f'#{t+1} {min_room_num} {max_visited}')