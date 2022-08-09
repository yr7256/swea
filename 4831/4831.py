import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))+[N]  # out of range 방지
    fuel = K  # 시작은 완충.
    point = 0  # 버스가 어딨는지. (for문에서 계속 갱신)
    count = 0  # 충전 얼마나 했는지.
    for i in range(M):
        if bus_stop[i]-point <= fuel:  # 지금 지점과 이전 지점의 길이보다 연료가 많을 때
            if bus_stop[i+1]-point > fuel:  # 다음 지점과 이전 지점 사이의 길이가 연료보다 많을 때
                fuel = K # 연료 충전하고 count+=1
                count += 1
            else:
                fuel -= (bus_stop[i]-point)  # 다음 지점과 이전 지점 사이의 길이보다 연료가 많으면 충전 필요x
            point = bus_stop[i]  # 지점 갱신
        else:  # 지금 지점과 이전 지점의 길이보다 연료보다 크다면 충전을 해도 더 이상 가지 못함.
            count = 0
            break
    print(f'#{t+1} {count}')

