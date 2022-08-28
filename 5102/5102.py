import sys
sys.stdin = open('sample_input.txt')


# def bfs(start):
#     queue = [start]
#     visited[start] = 1
#     while queue:
#         start = queue.pop(0)
#         for destination in range(1, V+1):
#             if adj[start][destination] and not visited[destination]:
#                 queue.append(destination)
#                 visited[destination] = visited[start] + 1
#     return

def bfs():
    queue = [[S, 0]]
    while queue:
        current, idx = queue.pop(0)
        if not visited[current]:
            visited[current] = 1
        for destination in edges[current]:
            if not visited[destination]:
                if destination == G:
                    return idx+1
                queue.append([destination, idx+1])
    return 0



T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    # adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    # for _ in range(E):
    #     a, b = map(int, input().split())
    #     adj[a][b] = 1
    #     adj[b][a] = 1
    # S, G = map(int, input().split())
    # # print(S, G)
    # bfs(S)
    # if visited[G]:
    #     ans = visited[G]-1
    # else:
    #     ans = 0
    # print(f'#{t+1} {ans}')
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    S, G = map(int, input().split())
    print(f'#{t+1} {bfs()}')


