def rev(n):
    return n[::-1]


T = int(input())
for t in range(T):
    s = input()
    print(f'{t+1} {rev(s)}')