import sys
sys.stdin = open('input.txt')


def check(x, y):
    x0, y0 = x, y
    column, row = 1, 1
    while True:
        x += 1
        if 0 <= x < n and arr[x][y] and not visited[x][y]:
            column += 1
        else:
            x -= 1
            break
    while True:
        y += 1
        if 0 <= y < n and arr[x][y] and not visited[x][y]:
            row += 1
        else:
            y -= 1
            break
    for k in range(i, x+1):
        for l in range(j, y+1):
            visited[k][l] = True
    return [column, row]


T = int(input())
for t in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] and not visited[i][j]:
                result.append(check(i, j))
    result.sort(key=lambda x: (x[0]*x[1], x[0]))
    print(f'#{t+1} {len(result)}', end=' ')
    for i in result:
        print(*i, end=' ')
    print()
