dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
