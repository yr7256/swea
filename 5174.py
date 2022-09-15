def cnt(n):
    global ans
    if len(v[n]) == 0:
        return
    ans += len(v[n])
    for c in v[n]:
        cnt(c)


T = int(input())
for t in range(T):
    E, N = map(int, input().split())
    v = [[]*(E+2) for _ in range(E+2)]
    lst = list(map(int, input().split()))
    ans = 1
    for i in range(0, len(lst), 2):
        p, s = lst[i], lst[i+1]
        v[p].append(s)
    cnt(N)
    print(f'#{t+1} {ans}')