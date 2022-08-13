T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    time = [int(input()) for _ in range(N)]
    left, right = 1, max(time)*M
    while left <= right:
        mid = (left+right)//2
        temp = 0
        for ti in time:
            temp += mid//ti
        if temp < M:
            left = mid+1
        else:
            right = mid-1
    print(f'#{t+1} {left}')
