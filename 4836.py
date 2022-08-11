T = int(input())                                       # test case 개수
for t in range(T):                                     #
    N = int(input())                                   # 색칠할 영역의 개수
    field = [[0]*10 for _ in range(10)]                # 색칠할 10*10 field를 생성
    for _ in range(N):                                 #
        x0, y0, x1, y1, c = map(int, input().split())  # x0,y0은 왼쪽 아래, x1,y1은 오른쪽 위 좌표, c는 색칠할 색
        for i in range(x0, x1+1):                      # x0에서 x1까지 y0에서 y1까지 영역에 색칠하기
            for j in range(y0, y1+1):                  #
                field[i][j] += c                       #
    ans = 0                                            # 보라색이 된 칸 개수 세기
    for r in field:                                    #
        for num in r:                                  #
            if num == 3:                               # 같은 색인 영역은 겹치치 않으므로 field에서 요소가 3인 것을 찾으면 된다
                ans += 1                               #
    print(f'#{t+1} {ans}')                             #