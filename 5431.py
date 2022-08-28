T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    people = [i for i in range(1, N+1)]
    submit = list(map(int, input().split()))
    print(f'#{t+1}', *[x for x in people if x not in submit])

