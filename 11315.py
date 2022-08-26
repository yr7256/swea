def check():
    ans = 'NO'
    for i in range(N):
        temp_row = ''
        temp_column = ''
        for j in range(N):
            temp_row += arr[i][j]
            temp_column += arr[j][i]
        if 'ooooo' in temp_row:
            ans = 'YES'
        if 'ooooo' in temp_column:
            ans = 'YES'
        temp_diag_one = ''                      # 오른쪽 아래로 가는 대각선인데 오른쪽으로 이동
        temp_diag_two = ''                      # 오른쪽 아래로 가는 대각선인데 왼쪽으로 이동
        temp_diag_three = ''                    # 왼쪽 아래로 가는 대각선인데 오른쪽으로 이동
        temp_diag_four = ''                     # 왼쪽 아래로 가는 대각선인데 왼쪽으로 이동
        for k in range(N-i):
            temp_diag_one += arr[k][k+i]
            temp_diag_two += arr[k+i][k]
            temp_diag_three += arr[k+i][N-k-1]
            temp_diag_four += arr[k][N-k-1-i]
        if 'ooooo' in temp_diag_one:
            ans = 'YES'
        if 'ooooo' in temp_diag_two:
            ans = 'YES'
        if 'ooooo' in temp_diag_three:
            ans = 'YES'
        if 'ooooo' in temp_diag_four:
            ans = 'YES'

    return ans


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{t+1} {check()}')