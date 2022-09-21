import sys
sys.stdin = open('sample_input.txt')


T = int(input())
lst = [i*i+(i-1)*(i-1) for i in range(50)]                      # 운영비용 그냥 넉넉하게 50정도까지 만들기 (도시 최대크기일때도 덮을수 있게)
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append([i, j])                             # 집 위치 저장
    ans = 0
    for k in range(1, 2*N-1):                                   # 왼쪽 아래에서 오른쪽 위까지 거리가 2N-2니까 끝까지 확인하자
        for i in range(N):
            for j in range(N):
                count = 0
                for x, y in home:
                    if abs(x-i) + abs(y-j) < k:                 # 집의 위치랑 임의의 점사이의 절대값 거리를 찾기 (마름모꼴 확인하는 작업)
                        count += 1                              # 맞다면 일단 count += 1 해주고
                if M * count - lst[k] >= 0:                     # count의 수*서비스 제공비 - 운영비용이 0보다 크거나 같다면 (손해를 보지않는다고 했으니)
                    ans = max(ans, count)                       # ans 계속 갱신해준다
    print(f'#{t+1} {ans}')

'''
마름모꼴 추가설명 : 어차피 마름모꼴에 있는 좌표들을 arr 넘어서까지 볼 필요가 없다. 그냥 안에 있는 요소들이 k보다 작으면 된다.
대충 설명하자면 이런 느낌
43234
32123
21012
32123
43234
'''