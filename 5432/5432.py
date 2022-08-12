T = int(input())                      # test case 개수
for t in range(T):                    #
    S = list(input())                 #
    stack = []                        # 쇠막대기를 담는 리스트
    answer = 0                        # 잘려진 개수를 저장하는 수
    for i in range(len(S)):           #
        if S[i] == '(':               # ( 면 stack에 넣기
            stack.append('(')         #
        else:                         # S[i] == ')' 일 때
            if S[i-1] == '(':         # () 일때 자른다!
                stack.pop()           # ex ((( () 라면 스택에 4개 들어가 있는데 3개 잘라야 하니까 pop
                answer += len(stack)  # stack에 있는 개수만큼 더해주기
            else:                     # ) ) 이면 쇠막대기 하나 다 잘린거.(나머지 조각 1개 나온다)
                stack.pop()           # 그래서 stack을 pop하고
                answer += 1           # stack에 1 더해주기
    print(f'#{t+1} {answer}')         #
