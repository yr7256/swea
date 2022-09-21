T = int(input())
for t in range(T):
    N = int(input())
    temp = int(N**(1/3))
    ans = -1
    for i in range(temp, temp+2):
        if i**3 == N:
            ans = i
            break
    print(f'#{t+1} {ans}')