def preorder(x):
    if x != '.':
        print(x, end=' ')
        preorder(tree[x][0])
        preorder(tree[x][1])


V = int(input())
tree = {}
for i in range(V):
    tree[i+1] = ['.', '.']
edges = list(map(int, input().split()))
for i in range(0, len(edges), 2):
    root, node = edges[i], edges[i+1]
    tree[root] += [node]
    if len(tree[root]) == 3:
        tree[root].pop(0)
preorder(1)
