def dijkstra():
    dist = [987654321] * (V+1)
    dist[0] = 0  # 여기 start 점을 넣어주면 됨.
    visited = [False] * (V+1)

    for _ in range(V+1):
        min_idx = -1
        min_value = 987654321

        for i in range(V+1):  # 일단 현재 dist 배열에서 visited 안된애들 중 가장 노드 찾는 로직
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]  # 갱신!

        visited[min_idx] = True  # 가장 작은애로 이동할거니까 visited 넣어주고
        # 요거 주석 풀어서 visted, dist 찍어볼것!
        # print(visited, dist)

        # 이제 그 선택된 점에서부터 갈 수 있되, 그 가중치를 더하더라도 더 짧음을 보장한다면 dist 배열 갱신
        for i in range(V+1):
            if not visited[i] and dist[i] > adj[min_idx][i] + dist[min_idx]:
                dist[i] = adj[min_idx][i] + dist[min_idx]

    return dist[V]  # 도착점


for tc in range(1, int(input())+1):
    V, E = map(int,input().split())

    adj = [[987654321] * (V+1) for _ in range(V+1)]  # inf 개념으로 큰 수 넣어줌

    for i in range(E):  # 인접행렬 만들기
        st, ed, w = map(int, input().split())
        adj[st][ed] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화

    print("#{} {}".format(tc, dijkstra()))