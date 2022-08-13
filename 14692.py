T = int(input())
for t in range(T):
    N = int(input())
    w = ''
    if N % 2:
        w = 'Bob'
    else:
        w = 'Alice'
    print(f'#{t+1} {w}')
