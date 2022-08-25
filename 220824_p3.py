from collections import deque


def bfs(queue, visited, adj_matrix):
    while queue:
        start = queue.popleft()
        if start not in visited:
            visited.append(start)
        for destination in range(1, V+1):
            if adj_matrix[start][destination] and destination not in visited:
                queue.append(destination)
    return visited


V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
edge = list(map(int, input().split()))
for i in range(0, E*2, 2):
    adj[edge[i]][edge[i+1]] = 1
    adj[edge[i+1]][edge[i]] = 1
print(*bfs(deque([1]), [], adj))
