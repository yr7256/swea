T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        temp = 0
        for j in range(M):
            if arr[i][j]:
                temp += 1
                if ans < temp:
                    ans = temp
            else:
                temp = 0
    for j in range(M):
        temp = 0
        for i in range(N):
            if arr[i][j]:
                temp += 1
                if ans < temp:
                    ans = temp
            else:
                temp = 0
    print(f'#{t+1} {ans}')
