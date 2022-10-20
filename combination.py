# arr = ['A', 'B', 'C']
# for i in range(3):
#     for j in range(i+1, 3):
#         print(arr[i], arr[j])
#
# for i in range(3):
#     for j in range(i, 3):
#         print(arr[i], arr[j])

arr = ['A', 'B', 'C', 'D', 'E']
sel = [0, 0, 0]


def combination(idx, sidx):
    if sidx == 3:
        print(sel)
        return
    if idx == 5:
        return

    sel[sidx] = arr[idx]
    combination(idx+1, sidx+1)
    combination(idx+1, sidx)


combination(0, 0)


def combi_rep(idx, sidx):
    if sidx == m:
        print(*sel)
        return

    if idx == n:
        return

    sel[sidx] = arr[idx]
    combi_rep(idx, sidx+1)
    combi_rep(idx+1, sidx)


n, m = map(int, input().split())
arr = list(range(1,n+1))
sel = [0]*m
combi_rep(0, 0)