from collections import deque

T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    tunnels = {
        1: [1, 1, 1, 1],
        2: [0, 1, 0, 1],
        3: [1, 0, 1, 0],
        4: [1, 0, 0, 1],
        5: [1, 1, 0, 0],
        6: [0, 1, 1, 0],
        7: [0, 0, 1, 1]
    }
    print(arr)  