import sys


T = int(input())                              # test case 개수
for t in range(T):                            #
    N = int(input())                          # 리스트의 요소 개수
    N_list = list(map(int, input().split()))  # 매매가의 리스트
    max_N = N_list[-1]                        # 맨 뒤를 최대값으로 정하자 (미래는 알 수 없으니까)
    ans = 0                                   # 번 돈을 저장하는 수
    for i in range(N-2, -1, -1):              # 맨 뒤는 돌 필요 없으므로 맨 뒤에서 두번째부터 처음까지 돈다
        if max_N > N_list[i]:                 # 최댓값보다 요소가 적으면
            ans += max_N-N_list[i]            # ans에 더한다
        else:                                 # 최댓값보다 요소가 크면
            max_N = N_list[i]                 # 최댓값 갱신
    print('#%d %d' %(t+1, ans))               #