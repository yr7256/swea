T = int(input())                        #
for t in range(T):                      #
    S = input()                         #
    stack = []                          #
    for i in S:                         #
        if stack and stack[-1] == i:    # 아이디어 : 대부분의 경우에서는 원소를 stack에 넣지만,
            stack.pop()                 # stack의 끝과 i가 같다면 i를 stack에 넣지않고 뽑는다!
        else:                           #
            stack.append(i)             #
    print(f'#{t+1} {len(stack)}')       #