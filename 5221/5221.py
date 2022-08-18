import sys
sys.stdin = open('input.txt')
for _ in range(10):
    T, E = map(int, input().split())
    graph = [[0]*100 for _ in range(100)]
    visited = [0]*100
    edge = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        graph[edge[i]][edge[i+1]] = 1
    queue = [0]
    while queue:
        current = queue.pop()
        visited[current] = 1
        for i in range(100):
            if visited[i] == 0 and graph[current][i]:
                queue.append(i)
    print(f'#{T} {visited[99]}')
