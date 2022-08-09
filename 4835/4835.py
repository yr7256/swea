import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # test case 개수
for t in range(T):
    N, M = map(int, input().split())  # N은 정수의 개수, M은 구간의 개수
    nums = list(map(int, input().split()))
    sum_min = 1000000  # 구간의 최대합과 최소합을 갱신해주기로 함.
    sum_max = 0
    for i in range(N-M+1):  # temp = nums[i]+nums[i+1]+...+nums[i+M-1] <- 이 아이디어로 접근함.
        temp = 0  # temp는 구간합을 저장해주는 수.
        for j in range(M):
            # 이렇게 하면 i==0일 때, temp=nums[0+0]+nums[0+1].. 이런식으로 합해지고
            # 최소값 최대값 갱신 후, temp가 다시 0이 된다.
            temp += nums[i+j]
        if sum_min > temp:  # 최소값 갱신
            sum_min = temp
        if sum_max < temp:  # 최대값 갱신
            sum_max = temp
    print(f'#{t+1} {sum_max - sum_min}')