import sys
sys.stdin = open('input.txt')
T = int(input())                                               # test case 개수
standard = [i for i in range(1, 10)]                           # 1,2,3,4,5,6,7,8,9 검사할 리스트
for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]  # 스도쿠 배열 받기
    ans = 0                                                    # 완성 되는지 안되는지
    count = 0                                                  # 사각형 9개 가로 9개 세로 9개 만족하는지
    for i in range(0, 9, 3):                                   # 사각형 검사
        for j in range(0, 9, 3):                               # [00 01 02, 10 11 12, 20 21 22] 이런식으로 한세트를 구성
            temp_square = []                                   # 사각형 요소를 넣을 빈 리스트
            for k in range(3):                                 #
                for l in range(3):                             #
                    temp_square.append(arr[i+k][j+l])          #
            if sorted(temp_square) == standard:                # 만약 이 사각형이 1,2,3,4,5,6,7,8,9 라면 count+=1
                count += 1
            else:                                              # 아니라면 바로 break
                break
    for i in range(9):                                         # 가로 세로 체크하기
        temp_row = []
        temp_column = []
        for j in range(9):
            temp_row.append(arr[i][j])
            temp_column.append(arr[j][i])
        if sorted(temp_row) == standard:                       # 가로 체크하기
            count += 1
        if sorted(temp_column) == standard:                    # 세로 체크하기
            count += 1
    if count == 27:                                            # 사각형 가로 세로 모두 만족하면 ans = 1
        ans = 1
    print(f'#{t+1} {ans}')



