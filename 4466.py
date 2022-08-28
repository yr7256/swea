T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(f'#{t+1} {sum(nums[:K])}')
