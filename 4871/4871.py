import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    for i in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1
    S, E = map(int, input().split())
    queue = [S]
    while queue:
        current = queue.pop()
        visited[current] = 1
        for i in range(1, V+1):
            if visited[i] == 0 and graph[current][i]:
                queue.append(i)
    print(f'#{t+1} {visited[E]}')
