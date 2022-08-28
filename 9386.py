T = int(input())
for t in range(T):
    N = int(input())
    S = input()
    count = 1
    max_cnt = 1
    for i in range(N-1):
        if S[i] == S[i+1] == '1':
            count += 1
            max_cnt = max(max_cnt, count)
        else:
            count = 1
    print(f'#{t+1} {max_cnt}')

