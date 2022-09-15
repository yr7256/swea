def inorder(n):
    global num
    if n <= N:
        inorder(n*2)
        tree[num+1][0] = n
        num += 1
        inorder(n*2+1)


T = int(input())
for t in range(T):
    N = int(input())
    tree = [[0, i] for i in range(N+1)]
    num = 0
    inorder(1)
    print(tree)
    tree.sort()
    print(tree)
    print(f'#{t+1} {tree[1][1]} {tree[N//2][1]}')