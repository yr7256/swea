import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp += arr[i+k][j+l]
            ans = max(temp, ans)
    print(f'#{t+1} {ans}')

