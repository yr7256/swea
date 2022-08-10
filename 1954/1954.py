dx = [0, 1, 0, -1]                                       # dx와 dy를 만들어 x,y 방향을 정히려고 함.
dy = [1, 0, -1, 0]                                       # 순서는 우하좌상이므로 (0,1),(1,0),(0,-1),(-1,0)이 된다.
T = int(input())                                         # test case의 수
for t in range(T):                                       #
    N = int(input())                                     #
    arr = [[0]*N for _ in range(N)]                      # 숫자를 저장할 N*N 배열 만들기.
    count = 1                                            # 조건을 만족했을 때, x,y가 찍어줄 숫자.
    x, y = 0, 0                                          # 초기 x,y 값 (이 x,y가 돌면서 숫자를 찍어줄 것이다.)
    direction = 0                                        # dx,dy의 방향을 정해줄 수. (오른쪽 가는 것이 시작이므로 초기값은 0)
    while count <= N**2:                                 # N*N 배열이므로 N**2만큼 돌면 모든 요소에 방문할 것이다.
        if 0 <= x < N and 0 <= y < N and not arr[x][y]:  # x,y는 배열안에서 돌아야 하고, 방문한 적이 없어야한다.
            arr[x][y] = count                            # 위의 조건을 만족한다면 그 요소에 count를 찍고,
            count += 1                                   # count+=1 하면서 다음 요소를 찾는다.
        else:                                            # x,y가 배열 밖으로 나가거나 이미 방문한 요소가 방문한다면
            x -= dx[direction]                           # 이동하기 이전으로 돌아가면서
            y -= dy[direction]                           # (while 가장 밑을 보면 x,y는 계속 증가하므로 그 수를 빼는 것.)
            direction += 1                               # 방향을 바꿔준다.
            direction %= 4                               # 만약 현재 방향이 3이라면 다음 방향은 0이어야 하므로 4로 나누어줬다.
        x += dx[direction]                               # 조건에 상관 없이 방향에 따라서 x,y 위치를 갱신해준다.
        y += dy[direction]                               #
    print(f'#{t+1}')                                     #
    for i in arr:                                        #
        print(*i)                                        # asterisk를 사용해 list를 unpacking 했다.