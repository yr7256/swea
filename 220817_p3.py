def dfs(start, visited, adj_matrix):
    visited.append(start)
    for destination in range(1, V+1):
        if adj[start][destination] and destination not in visited:
            visited = dfs(destination, visited, adj_matrix)
    return visited


V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
edge = list(map(int, input().split()))
for i in range(0, E*2, 2):
    adj[edge[i]][edge[i+1]] = 1
    adj[edge[i+1]][edge[i]] = 1
# stack = [1]
# visited = []
# while stack:
#     current = stack.pop()
#     if current not in visited:
#         visited.append(current)
#     for destination in range(V+1):
#         if adj[current][destination] and destination not in visited:
#             stack.append(destination)
# print(*visited)

print(*dfs(1, [], adj))


