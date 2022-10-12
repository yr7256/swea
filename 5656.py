from collections import deque
from copy import deepcopy
from itertools import product


def bfs(x, y, power):  # bfs 돌리면서 터뜨렸으면 0으로 (visited 필요가 없다)
    queue = deque([(x, y, power)])
    temp_arr[x][y] = 0
    while queue:
        x0, y0, p0 = queue.popleft()
        for k in range(1, p0):
            for i in range(4):
                x1 = x0+dx[i]*k
                y1 = y0+dy[i]*k
                if 0 <= x1 < H and 0 <= y1 < W and temp_arr[x1][y1]:
                    queue.append((x1, y1, temp_arr[x1][y1]))
                    temp_arr[x1][y1] = 0


def down(lst):  # 벽돌 내리기 맨 밑에서부터 탐색하면서 숫자 있으면 넣고 다시 그 위 칸부터 탐색
    down_board = [[0]*W for _ in range(H)]
    for j in range(W):
        target = H-1
        for i in range(H-1, -1, -1):
            if lst[i][j]:
                down_board[target][j] = lst[i][j]
                target -= 1
    return down_board


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for t in range(T):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    ans = W*H
    possible = list(product(range(W), repeat=N))  # 몇 번째 시도에 몇 번째 인덱스 폭탄 터뜨릴거냐
    for idx_lst in possible:
        temp_arr = deepcopy(arr)
        for idx in idx_lst:  # N번째까지 부수고 다시 처음으로 돌려서 작업하기(temp_arr 초기화)
            for i in range(H):
                if temp_arr[i][idx]:
                    bfs(i, idx, temp_arr[i][idx])
                    break
            temp_arr = down(temp_arr)  # 작업후에 벽돌 내리기
        temp = 0
        for i in range(H):
            for j in range(W):
                if temp_arr[i][j]:
                    temp += 1
        ans = min(ans, temp)
    print(f'#{t+1} {ans}')


