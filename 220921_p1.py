def Selection(A, s):
    n = len(A)
    if s == n-1:
        return
    min = s
    for i in range(s, n):
        if A[min] > A[i]:
            min = i
    A[s], A[min] = A[min], A[s]

    Selection(A, s+1)


A = [2, 4, 6, 1, 9, 8, 7, 0]
Selection(A, 0)
print(A)
