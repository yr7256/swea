N = int(input())
for i in range(N):
    s = input()
    temp = bin(int(s, 16))[2:]
    ans = '0'*(len(s)*4-len(temp))+temp
    print(ans)
    for i in range(0, len(ans), 7):
        print(int(ans[i:i+7], 2), end=' ')
    print()
