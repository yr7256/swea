for t in range(10):
    N = int(input())
    stack = []
    tree = [0]*(N+1)
    info = []
    for _ in range(N):
        i = input().split()
        if len(i) == 4:
            info.append(i)
        else:
            tree[int(i[0])] = int(i[1])
    # print(info)
    for i in range(len(info)-1, -1, -1):
        if info[i][1] == '+':
            tree[int(info[i][0])] = tree[int(info[i][2])] + tree[int(info[i][3])]
        if info[i][1] == '-':
            tree[int(info[i][0])] = tree[int(info[i][2])] - tree[int(info[i][3])]
        if info[i][1] == '*':
            tree[int(info[i][0])] = tree[int(info[i][2])] * tree[int(info[i][3])]
        if info[i][1] == '/':
            tree[int(info[i][0])] = tree[int(info[i][2])] / tree[int(info[i][3])]
    print(f'#{t+1} {int(tree[1])}')