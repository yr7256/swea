T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())), reverse=True)
    ans = [0]*M
    # ans = 0
    for i in range(N):
        for j in range(M):
            if w[i] <= t[j]:
                if not ans[j]:
                    ans[j] = w[i]
                    break
    print(f'#{tc+1} {sum(ans)}')
