for t in range(10):  # test case 10개
    N = int(input())
    building_list = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-2):  # 리스트의 처음 두개, 마지막 두개는 0이므로 돌지 않아도 된다.
        max_diff = 255  # 건물 최대 높이는 255니까 가장 큰 차도 255이다.
        for j in range(5):
            if j == 2:  # j==2일 때, i-i니까 안됨. (제외)
                continue
            else:
                diff_temp = building_list[i]-building_list[i-2+j]
                if max_diff > diff_temp:  # min,max 쓰지 않고 구현해보기
                    max_diff = diff_temp
        if max_diff > 0:  # 0보다 작거나 같다면 조망권 확보 x 이므로 더하면 안된다.
            answer += max_diff
    print(f'#{t+1} {answer}')
