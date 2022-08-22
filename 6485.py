T = int(input())
for t in range(T):
    N = int(input())
    route = []
    for i in range(N):
        A, B = map(int, input().split())
        route.append([A, B])
    P = int(input())
    C_list = [int(input()) for _ in range(P)]
    bus_stop = [0]*5001
    for i in route:
        for j in range(i[0], i[1]+1):
            bus_stop[j] += 1
    print(f'#{t+1}', end=' ')
    for i in C_list:
        print(bus_stop[i], end=' ')
    print()

# P : 정류장 개수
# N : 버스 노선 개수
# A 이상 B 이하 모든 정류장 다 다님 +=1
# 1
# 2
# 1 3
# 2 5
# 5
# 1
# 2
# 3
# 4
# 5
