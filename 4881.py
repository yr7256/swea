def perm(depth, acc):
    global answer
    if acc >= answer:
        return
    if depth == N:
        if answer > acc:
            answer = acc
        return
    for i in range(N):
        if not check[i]:
            check[i] = 1
            perm(depth+1, acc+arr[depth][i])
            check[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 100
    check = [0]*N
    perm(0, 0)
    print(f'#{t+1} {answer}')

# 다시 풀기
