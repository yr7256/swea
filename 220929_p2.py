from collections import deque


def bfs(n):
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x not in visited:
            visited.append(x)
        for i in range(max(V)+1):
            if arr[x][i] and i not in visited:
                queue.append(i)


V = list(map(int, input().split()))
arr = [[0]*(max(V)+1) for _ in range(max(V)+1)]
visited = []
for i in range(len(V)//2):
    arr[V[2*i]][V[2*i+1]] = 1
    arr[V[2*i+1]][V[2*i]] = 1
# queue = [1]
# while queue:
#     x = queue.popleft()
#     if x not in visited:
#         visited.append(x)
#     for i in range(max(V)+1):
#         if arr[x][i] and i not in visited:
#             queue.append(i)
bfs(1)
print(*visited)
