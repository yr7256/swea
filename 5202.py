T = int(input())
for t in range(T):
    N = int(input())
    info = []
    for i in range(N):
        s, e = map(int, input().split())
        info.append((s, e))
    info.sort(key=lambda x: x[1])
    check = info.pop(0)
    count = 1
    while info:
        if info[0][0] < check[1]:  # 다음이 더 길면 그냥 뽑아냄 (check할 필요없다)
            info.pop(0)
        else:
            check = info.pop(0)
            count += 1

    print(f'#{t+1} {count}')
