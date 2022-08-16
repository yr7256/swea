V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    adj[start][end] = 1
    adj[end][start] = 1
stack = [1]
visited = []
while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)
    for destination in range(V+1):
        if adj[current][destination] and destination not in visited:
            stack.append(destination)
print(visited)