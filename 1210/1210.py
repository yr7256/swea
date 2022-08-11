import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 0]                                                             # dx,dy 방향값 설정
dy = [0, -1, 1]                                                             # 기본은 위로 1은 왼쪽 2는 오른쪽
for t in range(10):                                                         # test case 개수
    N = int(input())                                                        #
    ladder = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]  # index error 방지하기 위해 양쪽에 0 넣기
    x, y = 0, 0                                                             # x, y 초기값 설정하기 위해 x, y 생성
    d = 0                                                                   # 초기 방향값 (위로 가는 것)
    for i in range(100):                                                    # 처음 시작할 x,y 지점 설정
        for j in range(102):                                                #
            if ladder[i][j] == 2:                                           #
                x, y = i, j                                                 #
    while True:                                                             #
        if x == 0:                                                          # x==0일 때, 사다리의 맨 위로 가니까 break
            break                                                           #
        if ladder[x][y-1]:                                                  # 좌표의 왼쪽에 1이 있다면
            d = 1                                                           # 방향값을 1로 설정 (왼쪽 방향)
            while True:                                                     # 계속 왼쪽으로 가다가
                x += dx[d]                                                  #
                y += dy[d]                                                  #
                if not ladder[x][y-1]:                                      # 왼쪽에 0이 있다면 break
                    break                                                   #
        elif ladder[x][y+1]:                                                # 좌표의 오른쪽에 1이 있다면
            d = 2                                                           # 방향값을 2로 설정 (오른쪽 방향)
            while True:                                                     # 계속 오른쪽으로 가다가
                x += dx[d]                                                  #
                y += dy[d]                                                  #
                if not ladder[x][y+1]:                                      # 오른쪽에 0이 있다면 break
                    break                                                   #
        d = 0                                                               # 기본은 계속 위로 가기
        x += dx[d]                                                          #
        y += dy[d]                                                          #
    print(f'#{t+1} {y-1}')                                                  #
