T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    box = [0]*(N+1)
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            box[j] = i+1
    print(f'#{t+1}', end=' ')
    for i in box[1:]:
        print(i, end=' ')
    print()
