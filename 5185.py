T = int(input())
for t in range(T):
    N, s = input().split()
    temp = bin(int(s, 16))[2:]
    ans = '0' * (len(s) * 4 - len(temp)) + temp
    print(f'#{t+1} {ans}')