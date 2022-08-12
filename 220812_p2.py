def abs_val(n):
    return n if n>=0 else -n


def itoa(n):
    abs_n = abs_val(n)
    ans = ''
    while abs_n > 0:
        a = abs_n % 10
        if n >= 0:
            ans += chr(a+48)
        else:
            ans += chr(a+48)
        abs_n //= 10
    return ans[::-1] if n >= 0 else '-'+ans[::-1]


T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t+1} {itoa(N)} {type(itoa(N))}')
