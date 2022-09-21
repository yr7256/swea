from collections import deque

T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]
    visited = [[0]*(M+2) for _ in range(N+2)]
    count = 0
    queue = deque()
    queue.append([R+1, C+1])
    visited[R+1][C+1] = 1
    while queue:
        x, y = queue.popleft()
        if arr[x][y] == 1:
            if (arr[x+1][y] == 1 or arr[x+1][y] == 2 or arr[x+1][y] == 4 or arr[x+1][y] == 7) and not visited[x+1][y]:
                queue.append([x+1, y])
                visited[x+1][y] = visited[x][y]+1
            if (arr[x-1][y] == 1 or arr[x-1][y] == 2 or arr[x-1][y] == 5 or arr[x-1][y] == 6) and not visited[x-1][y]:
                queue.append([x-1, y])
                visited[x-1][y] = visited[x][y]+1
            if (arr[x][y+1] == 1 or arr[x][y+1] == 3 or arr[x][y+1] == 6 or arr[x][y+1] == 7) and not visited[x][y+1]:
                queue.append([x, y+1])
                visited[x][y+1] = visited[x][y]+1
            if (arr[x][y-1] == 1 or arr[x][y-1] == 3 or arr[x][y-1] == 4 or arr[x][y-1] == 5) and not visited[x][y-1]:
                queue.append([x, y-1])
                visited[x][y-1] = visited[x][y]+1
        if arr[x][y] == 2:
            if (arr[x+1][y] == 1 or arr[x+1][y] == 2 or arr[x+1][y] == 4 or arr[x+1][y] == 7) and not visited[x+1][y]:
                queue.append([x+1, y])
                visited[x+1][y] = visited[x][y]+1
            if (arr[x-1][y] == 1 or arr[x-1][y] == 2 or arr[x-1][y] == 5 or arr[x-1][y] == 6) and not visited[x-1][y]:
                queue.append([x-1, y])
                visited[x-1][y] = visited[x][y]+1
        if arr[x][y] == 3:
            if (arr[x][y+1] == 1 or arr[x][y+1] == 3 or arr[x][y+1] == 6 or arr[x][y+1] == 7) and not visited[x][y+1]:
                queue.append([x, y+1])
                visited[x][y+1] = visited[x][y]+1
            if (arr[x][y-1] == 1 or arr[x][y-1] == 3 or arr[x][y-1] == 4 or arr[x][y-1] == 5) and not visited[x][y-1]:
                queue.append([x, y-1])
                visited[x][y-1] = visited[x][y]+1
        if arr[x][y] == 4:
            if (arr[x-1][y] == 1 or arr[x-1][y] == 2 or arr[x-1][y] == 5 or arr[x-1][y] == 6) and not visited[x-1][y]:
                queue.append([x-1, y])
                visited[x-1][y] = visited[x][y]+1
            if (arr[x][y+1] == 1 or arr[x][y+1] == 3 or arr[x][y+1] == 6 or arr[x][y+1] == 7) and not visited[x][y+1]:
                queue.append([x, y+1])
                visited[x][y+1] = visited[x][y]+1
        if arr[x][y] == 5:
            if (arr[x+1][y] == 1 or arr[x+1][y] == 2 or arr[x+1][y] == 4 or arr[x+1][y] == 7) and not visited[x+1][y]:
                queue.append([x+1, y])
                visited[x+1][y] = visited[x][y]+1
            if (arr[x][y+1] == 1 or arr[x][y+1] == 3 or arr[x][y+1] == 6 or arr[x][y+1] == 7) and not visited[x][y+1]:
                queue.append([x, y+1])
                visited[x][y+1] = visited[x][y]+1
        if arr[x][y] == 6:
            if (arr[x+1][y] == 1 or arr[x+1][y] == 2 or arr[x+1][y] == 4 or arr[x+1][y] == 7) and not visited[x+1][y]:
                queue.append([x+1, y])
                visited[x+1][y] = visited[x][y]+1
            if (arr[x][y-1] == 1 or arr[x][y-1] == 3 or arr[x][y-1] == 4 or arr[x][y-1] == 5) and not visited[x][y-1]:
                queue.append([x, y-1])
                visited[x][y-1] = visited[x][y]+1
        if arr[x][y] == 7:
            if (arr[x-1][y] == 1 or arr[x-1][y] == 2 or arr[x-1][y] == 5 or arr[x-1][y] == 6) and not visited[x-1][y]:
                queue.append([x-1, y])
                visited[x-1][y] = visited[x][y]+1
            if (arr[x][y-1] == 1 or arr[x][y-1] == 3 or arr[x][y-1] == 4 or arr[x][y-1] == 5) and not visited[x][y-1]:
                queue.append([x, y-1])
                visited[x][y-1] = visited[x][y]+1
    for i in visited:
        for j in i:
            if 0 < j <= L:
                count += 1
    print(f'#{t+1} {count}')

