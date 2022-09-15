T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)+[0]
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    for i in range(len(tree)//2-1, 0, -1):
        if not tree[i]:
            tree[i] = tree[2*i]+tree[2*i+1]
            # print(tree)
            # print(i)
    # print(tree)
    print(f'#{t+1} {tree[L]}')
