# def check():
#     stack = []
#     for i in S:
#         if i == '{' or i == '(':
#             stack.append(i)
#         if i == ')' or i == '}':
#             if stack:
#                 x = stack.pop()
#             else:
#                 return 0
#             if i == ')' and x == '{':
#                 return 0
#             if i == '}' and x == '(':
#                 return 0
#     if stack:
#         return 0
#     else:
#         return 1
#
#
# T = int(input())
# for t in range(T):
#     S = input()
#     print(f'#{t+1} {check()}')


T = int(input())                        # test case의 개수
for t in range(T):                      #
    S = input()                         # 괄호검사 해야할 문자열
    stack = []                          # 괄호들을 넣을 list
    ans = 1                             # 기본은 1로 설정
    for i in S:                         #
        if i == '{' or i == '(':        # 문자열이 열린 괄호일 때, stack에 넣는다.
            stack.append(i)             #
        if i == ')' or i == '}':        # 문자열이 닫힌 괄호일 때
            if stack:                   # stack에 원소가 있다면
                x = stack.pop()         # 일단 pop한 다음 그 원소를 x라고 한다.
            else:                       # 아니라면
                stack.append(i)         # stack에 닫힌 괄호 하나 넣고 break
                break                   # (기본이 1이고 stack에 원소 없을 때도 1이기 때문에 원소를 채워줘야 함)
            if i == ')' and x == '{':   # 짝이 안맞을 경우에도
                stack.append(i)         # stack에 닫힌 괄호 하나 넣고 break
                break                   #
            if i == '}' and x == '(':   #
                stack.append(i)         #
                break                   #
    if stack:                           # 다 돈 다음에 stack에 원소가 있다면 0
        ans = 0                         #
    else:                               # 없다면 1
        ans = 1                         #
    print(f'#{t+1} {ans}')              #
