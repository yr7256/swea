import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    start, end = N//2, N//2
    for i in range(N):
        for j in range(start, end+1):
            ans += arr[i][j]
        if i < N//2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f'#{t+1} {ans}')
