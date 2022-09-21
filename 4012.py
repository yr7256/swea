from itertools import combinations

T = int(input())
for t in range(T):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    foods = []
    gap = 1000000000
    for i in list(combinations(range(N), N//2)):
        foods.append(i)
    for a in foods:
        foods_A = 0
        foods_B = 0
        for i in a:
            for j in a:
                if i == j:
                    continue
                foods_A += S[i][j]
        b = [i for i in range(N) if i not in a]
        for i in b:
            for j in b:
                if i == j:
                    continue
                foods_B += S[i][j]
        gap = min(gap, abs(foods_A - foods_B))
    print(f'#{t+1} {gap}')