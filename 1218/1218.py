import sys                                          # 처음 아이디어 : dict형으로 괄호를 한몸이라고 생각한다면
sys.stdin = open('input.txt')                       # 4873 반복문자 지우기와 똑같지 않을까?
for t in range(10):                                 # 10개의 test case
    N = int(input())                                #
    S = input()                                     # 판별할 문자열
    stack = []                                      # 문자열을 넣을 list
    dic = {')': '(', '}': '{', ']': '[', '>': '<'}  # 괄호의 쌍을 넣은 dict (괄호 세트를 한 몸이라고 생각하자)
    for i in S:                                     #
        if stack and stack[-1] == dic.get(i):       # stack에 원소가 있고 stack의 끝이 i의 value와 같다면
            stack.pop()                             # stack 뽑아내기 (pop은 비어있을 때 못하니까)
        else:                                       # 그게 아니라면 원소 집어넣기
            stack.append(i)                         #
    if stack:                                       # 끝까지 확인해서 stack이 차있다면 0 출력
        print(f'#{t + 1} 0')                        #
    else:                                           # 비어있다면 1 출력
        print(f'#{t + 1} 1')                        #

