def perm(depth, current, acc):
    global answer
    if acc >= answer:
        return
    if depth == N-1:
        answer = min(answer, acc+arr[current][0])
        return
    for i in range(N):
        if not check[i]:
            check[i] = 1
            perm(depth+1, i, acc+arr[current][i])
            check[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 1000
    check = [0]*N
    check[0] = 1
    perm(0, 0, 0)
    print(f'#{t+1} {answer}')
