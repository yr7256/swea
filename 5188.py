# def dfs(x, y, temp):
#     global ans
#     if temp > ans:
#         return
#     if x == N-1 and y == N-1:
#         ans = min(ans, temp)
#         return
#     for i in range(2):
#         x1 = x + dx[i]
#         y1 = y + dy[i]
#         if 0 <= x1 < N and 0 <= y1 < N:
#             dfs(x1, y1, temp+arr[x1][y1])
#
#
# dx = [1, 0]
# dy = [0, 1]
# T = int(input())
# for t in range(T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 190
#     dfs(0, 0, arr[0][0])
#     print(f'#{t+1} {ans}')


T = int(input())
for t in range(T):
    N = int(input())
    arr = [[100]*(N+2)]+[[100]+list(map(int, input().split()))+[100] for _ in range(N)]+[[100]*(N+2)]
    for i in range(N, -1, -1):
        for j in range(N, -1, -1):
            if i == j == N:
                continue
            arr[i][j] += min(arr[i+1][j], arr[i][j+1])
    print(f'#{t+1} {arr[1][1]}')
