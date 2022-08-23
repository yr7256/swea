T = int(input())
for t in range(T):
    S = input().split()
    stack = []
    ans = 0
    for i in S:
        if i.isnumeric():
            stack.append(int(i))
        else:
            try:
                if i == '*' or i == '+':
                    if i == '*':
                        stack.append(stack.pop() * stack.pop())
                    else:
                        stack.append(stack.pop() + stack.pop())
                elif i == '/' or i == '-':
                    x = stack.pop()
                    y = stack.pop()
                    if i == '/':
                        stack.append(y // x)
                    else:
                        stack.append(y - x)
            except IndexError:
                ans = 1
    if ans or len(stack) >= 2:
        print(f'#{t+1} error')
    else:
        print(f'#{t+1}', *stack)

