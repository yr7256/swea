T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    first = 0
    pizza = []
    ans = 0
    for i in enumerate(Ci, start=1):
        pizza.append(i)
    queue = pizza[:N]
    waiting = pizza[N:]
    while len(queue) > 1:
        num, ch = queue.pop(0)
        ch //= 2
        if ch:
            queue.append((num, ch))
        if not ch and len(waiting) >= 1:
            queue.append(waiting.pop(0))
    print(f'#{t+1} {queue[0][0]}')
