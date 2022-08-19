import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    zipped_arr = [[0]*N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            zipped_arr[i][j] = arr[j][i]
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 0:
                if count == K:
                    ans += 1
                count = 0
            else:
                count += 1
        if count == K:
            ans += 1

    for i in range(N):
        count = 0
        for j in range(N):
            if zipped_arr[i][j] == 0:
                if count == K:
                    ans += 1
                count = 0
            else:
                count += 1
        if count == K:
            ans += 1

    print(f'#{t+1} {ans}')