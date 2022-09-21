T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    arr = [input() for _ in range(N)]
    x, y = 0, 0
    flag = False
    for i in range(N):
        for j in range(M, -1, -1):
            if arr[i][j:j+7] in dic:
                x, y = i, j-49
                flag = True
                break
        if flag:
            break
    temp = 0
    ans = 0
    count = 0
    for i in range(y, y+56, 7):
        if count % 2:
            temp += dic[arr[x][i:i+7]]
        else:
            temp += dic[arr[x][i:i+7]]*3
        ans += dic[arr[x][i:i+7]]
        count += 1
    if temp % 10:
        print(f'#{t+1} 0')
    else:
        print(f'#{t+1} {ans}')