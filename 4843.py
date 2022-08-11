T = int(input())                                     # test case 개수
for t in range(T):                                   #
    N = int(input())                                 # 원소의 개수
    nums = list(map(int, input().split()))           # 원소를 받을 리스트
    for i in range(N):                               # bubble sort
        for j in range(i+1, N):                      # 오름차순 정렬
            if nums[i] > nums[j]:                    # 
                nums[i], nums[j] = nums[j], nums[i]  #
    print(f'#{t+1}', end=' ')                        #
    for n in range(5):                               #
        print(nums[N - n - 1], nums[n], end=' ')     # (뒤에서 i번째 수, 앞에서 i번째 수 한번에 출력하기) * 5
    print()                                          # 줄바꿈
