T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    lst = []
    s = input()*2
    for i in range(N//4):
        for j in range(0, N, N//4):
            lst.append(s[i+j:i+j+(N//4)])
    lst = list(set(lst))
    num_lst = []
    for i in lst:
        num_lst.append(int(i, 16))
    num_lst = sorted(num_lst, reverse=True)
    print(f'#{t+1} {num_lst[K-1]}')