import sys
sys.stdin = open('input.txt')


def inorder(n):
    if n <= N:
        inorder(n*2)
        print(n, end=' ')
        inorder(n*2+1)


for t in range(10):
    N = int(input())
    tree = [0]*(N+1)
    for i in range(N):
        info = input().split()
        tree[int(info[0])] = info[1]
    print(tree)
    print(f'#{t+1}', end=' ')
    inorder(1)
    print()
