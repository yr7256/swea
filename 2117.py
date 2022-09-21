T = int(input())
lst = [i*i+(i-1)*(i-1) for i in range(50)]
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append([i, j])
    ans = 0
    for k in range(1, 2*N-1):
        for i in range(N):
            for j in range(N):
                count = 0
                for x, y in home:
                    if abs(x-i) + abs(y-j) < k:
                        count += 1
                if M * count - lst[k] >= 0:
                    ans = max(ans, count)
    print(f'#{t+1} {ans}')