N = int(input())
for i in range(N):
    s=input()
    for i in range(0,len(s),7):
        print(int(s[i:i+7],2), end=' ')
    print()