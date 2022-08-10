T = int(input())                            # test case의 개수
for t in range(T):                          #
    nums = list(map(int, input().split()))  # 10개의 정수를 받을 리스트
    ans = 0                                 # 요소의 합이 0인 부분집합이 존재하는지
    for i in range(1 << 10):                # 비트 연산 이용해 부분집합 구하기.
        sum_sub = 0                         # 부분 집합의 원소의 합 저장해줄 수
        len_sub = 0                         # 부분 집합의 길이를 저장해줄 수
        for j in range(10):                 # nums의 요소에서
            if i & (1 << j):                # i의 j번째 비트가 1이라면
                sum_sub += nums[j]          # 원소의 합에 요소 더해주고
                len_sub += 1                # 길이도 1 더해준다.
        if sum_sub == 0 and len_sub:        # 합이 0이고 len_sub>0이라면 (공집합 제외)
            ans = 1                         # 더 돌 필요가 없으므로
            break                           # ans = 1 하고 break.
    print(f'#{t+1} {ans}')                  # f-string 사용