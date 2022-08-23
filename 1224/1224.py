# 후위 표기식 만들기!
# 위의 문제와 같이 곱셈 나눗셈일때는 append, 덧셈 뺄셈일때는 pop하고 append인데
# 괄호를 잘 생각해야한다. 괄호는 출력에 포함이 안되지만 연산할때 먼저 해야하는걸 기억하자.
# (6+5*(2-8)/2) 를 생각해보자.
# 열린 괄호일 때 일단 stack에 괄호를 넣어보자. (나중에 출력할때는 빼고 출력하면 되니까)
# 그리고 6+5*는 result에 65, stack에 (,+,* 넣고, 뒤를 생각해보자.
# 다시 열린 괄호일때 ( 넣고 2-8은 result에 6528, stack에 (,+,*,(,- 넣자.
# 닫힌 괄호 나오면 열린 괄호 나올때까지 뽑는거 생각하기.
# 그러므로 result는 6528- stack은 (,+,*
# 여기서 곱셈이나 나눗셈 나왔을 때는 앞에 있는 곱셈이나 나눗셈 먼저 더해줘야 출력과 같아지므로
# 곱셈 혹은 나눗셈이 나왔을 때, 마지막이 곱셈 혹은 나눗셈이라면 그거부터 더해주면
# result는 6528-*2 stack은 (,+,/
# 이제 숫자 없으니까 열린 괄호는 그냥 뽑아내고 다른 원소는 더해주면
# result는 6528-*2/+
# 후위 표기식 푸는 법은 쉽다.
# 숫자면 stack에 넣고 곱셈이나 덧셈 연산자가 나오면 숫자 두개 빼서
# 곱하거나 더해서 stack에 다시 넣으면 됨.
# 그래서 마지막 남은 원소 하나 뽑으면 끝.

import sys
sys.stdin = open('input.txt')
for t in range(10):
    N = int(input())
    S = input()
    result = ''
    stack = []
    for i in S:
        if i.isnumeric():
            result += i
        elif i == '(':
            stack.append(i)
        elif i == '*':
            while stack and stack[-1] == '*':
                result += stack.pop()
            stack.append(i)
        elif i == '+':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
    print(result)
    while stack:
        result += stack.pop()
    stack2 = []
    for i in result:
        if i.isnumeric():
            stack2.append(int(i))                       # int형으로 받아야함! (기본이 str)
        elif i == '*':
            stack2.append(stack2.pop()*stack2.pop())
        else:
            stack2.append(stack2.pop()+stack2.pop())
    # print(type(stack2[0]))
    print(f'#{t+1}', *stack2)
