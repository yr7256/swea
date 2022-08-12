T = int(input())                         # test case 개수
for t in range(T):
    board = [['']*15 for _ in range(5)]  # 최대 길이 : 15, 문자열의 개수 : 5 이므로 15*5 배열을 만든다
    for i in range(5):                   #
        s = input()                      # 문자열
        for j in range(len(s)):          # 문자열의 길이만큼 배열에 넣기
            board[i][j] = s[j]           #
    ans = ''                             # 전치를 넣을 빈 문자열 생성
    for i in range(15):
        for j in range(5):
            ans += board[j][i]
    print(f'#{t+1} {ans}')



