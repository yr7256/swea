from collections import deque


def bfs(n):
    queue = deque([n])
    visited[n] = 0
    while queue:
        x = queue.popleft()
        for current in adj[x]:
            if not visited[current]:
                visited[current] = visited[x]+1
                queue.append(current)


for t in range(10):
    N, start = map(int, input().split())
    lst = list(map(int, input().split()))
    visited = [0]*101
    adj = [[] for _ in range(101)]
    for i in range(0, N, 2):
        adj[lst[i]].append(lst[i+1])
    bfs(start)
    # print(adj)
    # print(visited)
    max_visited = max(visited)
    ans = 0
    for v in range(len(visited)):
        if visited[v] == max_visited:
            ans = max(ans, v)
    print(f'#{t+1} {ans}')
