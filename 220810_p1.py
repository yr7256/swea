def abs_val(n):                                                # 절댓값을 구하는 함수
    return n if n > 0 else -n                                  # 0보다 크면 자기 자신 작거나 같으면 -n 출력


dx = [1, 0, -1, 0]                                             # 방향을 설정해주기 위해 dx,dy 사용함
dy = [0, 1, 0, -1]                                             # 순서는 상관없음
T = int(input())                                               # test case 갯수
for t in range(T):
    N = int(input())                                           # 배열의 가로세로를 저장하는 수
    arr = [list(map(int, input().split())) for _ in range(N)]  # N*N 배열 저장
    sum_abs = 0                                                # 절댓값을 저장하는 수
    for i in range(N):                                         #
        for j in range(N):                                     #
            for k in range(4):                                 # 4방향에서 돌아가니까 range(4)
                x = i + dx[k]                                  # i, j에 방향값 더한 수를 각각 x, y라고 함
                y = j + dy[k]
                if 0 <= x < N and 0 <= y < N:                  # x, y가 배열안에 있으면 sum_abs에 절댓값 더함
                    sum_abs += abs_val(arr[i][j]-arr[x][y])    # (배열 넘어가면 무시함)
    print(f'#{t+1} {sum_abs}')