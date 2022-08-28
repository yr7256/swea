import sys
sys.stdin = open('input.txt')
dx = [1, 0, 0]
dy = [0, -1, 1]
for t in range(10):
    N = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    d = 0
    min_num = 10000
    ans = 0
    for i in range(102):
        if arr[0][i] == 1:
            x, y, count = 0, i, 0
            while True:
                if x == 99:
                    break
                if arr[x][y-1]:
                    d = 1
                    while True:
                        x += dx[d]
                        y += dy[d]
                        count += 1
                        if not arr[x][y-1]:
                            break
                elif arr[x][y+1]:
                    d = 2
                    while True:
                        x += dx[d]
                        y += dy[d]
                        count += 1
                        if not arr[x][y+1]:
                            break
                d = 0
                x += dx[d]
                y += dy[d]
                count += 1
            min_num = min(min_num, count)
            if min_num == count:
                ans = i
    print(f'#{t+1} {ans}')
