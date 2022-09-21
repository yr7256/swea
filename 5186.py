from math import isclose
T = int(input())
for t in range(T):
    N = float(input())
    ans = ''
    while True:
        N *= 2
        if isclose(N, 0):
            break
        if len(ans) > 12:
            ans = 'overflow'
            break
        if N >= 1:
            N -= 1
            ans += '1'
        else:
            ans += '0'
    print(f'#{t+1} {ans}')