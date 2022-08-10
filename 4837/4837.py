T = int(input())                           # test case 개수
nums = [i for i in range(1, 13)]           # 1부터 12까지의 숫자를 받는 리스트 생성 (부분집합의 합 구하기 위해서)
for t in range(T):                         #
    N, K = map(int, input().split())       # N개의 원소를 가지고 있고 합이 K인 부분집합의 개수 구하기
    count = 0                              # 조건에 해당하는 부분집합의 개수 카운트해주는 수
    for i in range(1 << len(nums)):        # 비트연산 이용해 부분집합 구하기
        sum_sub = 0                        # 부분 집합의 합 저장해줄 수
        len_sub = 0                        # 부분 집합의 길이 저장해줄 수
        for j in range(len(nums)):         # nums의 요소 중에서
            if i & (1 << j):               # i의 j번째 비트가 1이면
                sum_sub += nums[j]         # 그 요소만큼 sum_sub에 더해주고
                len_sub += 1               # 길이를 +1 해준다
        if len_sub == N and sum_sub == K:  # 길이가 N이고 합이 K인 부분집합을 찾았다면
            count += 1                     # count+=1 해준다
    print(f'#{t+1} {count}')               #

