from collections import deque
from copy import deepcopy


def bfs(x, y):
    global ans
    queue = deque([(x, y, 1, arr[x][y])])
    while queue:
        x0, y0, l0, current = queue.popleft()
        ans = max(ans, l0)
        for i in range(4):
            x1 = x0+dx[i]
            y1 = y0+dy[i]
            if 0 <= x1 < N and 0 <= y1 < N and arr[x1][y1] < current:
                queue.append((x1, y1, l0+1, arr[x1][y1]))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    h = 0
    ans = 0
    h_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == h:
                h_list.append((i, j))
            elif arr[i][j] > h:
                h_list = [(i, j)]
                h = arr[i][j]
    for i in range(N):
        for j in range(N):
            ori_arr = deepcopy(arr)
            for _ in range(1, K+1):
                arr[i][j] -= 1
                for x, y in h_list:
                    if (i, j) == (x, y):
                        continue
                    bfs(x, y)
            arr = ori_arr
    print(f'#{t+1} {ans}')


