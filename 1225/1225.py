import sys
sys.stdin = open('input.txt')
for _ in range(10):
    T = int(input())
    password = list(map(int, input().split()))
    count = 1
    while True:
        if count > 5:
            count = 1
        num = password.pop(0)-count
        if num <= 0:
            password.append(0)
            break
        password.append(num)
        count += 1
    print(f'#{T}', *password)
