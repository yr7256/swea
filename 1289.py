T = int(input())
for t in range(T):
    s = input()
    count = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            count += 1
    if s[0] == '1':
        print(f'#{t+1} {count+1}')
    else:
        print(f'#{t+1} {count}')