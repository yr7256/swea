def perm(depth):
    if depth == 2:
        print(sel)
        return

    for i in range(4):
        if not check[i]:
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth+1)
            check[i] = 0


N = 4
arr = ['A', 'B', 'C', 'D']
sel = [0] * 2
check = [0] * 4


perm(0)
