# ex) 9+5*2+5*3*4+1 면 952*+534**+1+
# 후위 표기식 만들 때, 숫자는 일단 그냥 넣고
# 곱셈은 일단 스택에 넣는다고 생각해보자.
# 근데 곱셈이 먼저니까 곱셈은 일단 stack에 넣고
# 덧셈 나오면 빼는 식으로 하면 되지 않을까.
# ex) 9+5*2+1 일 때 952 저장하고
# 스택에 +*넣고 + 나오면 +* 빼기 -> 952*+ 그리고 다시 1넣고
# 남은건 뒤에 넣으면 되니까 while 넣어서 pop으로 뽑아내자.
# (예를 들어, 9+5*2 라면 952 들어가고 stack에 +* 들어가니까 pop으로 빼면 된다.)
# 9+5*2+5*3*4+1 면 952*+534**+1+ 이런식으로 된다.
# 그러면 52* 는 10으로 저장될거고 534**는 앞에서 곱하든
# 뒤에서 곱하든 똑같으니까 5(34*)* 이런느낌으로 생각해보자

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
        elif i == '*':
            stack.append(i)
        else:
            while stack:
                result += stack.pop()
            stack.append(i)
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


