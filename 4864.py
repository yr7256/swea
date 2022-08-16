T = int(input())            # test case 개수
for t in range(T):          #
    N = input()             #
    M = input()             #
    if N in M:              # M 안에 N이 있으면
        print(f'#{t+1} 1')  # 1 출력
    else:                   # 없으면
        print(f'#{t+1} 0')  # 0 출력
