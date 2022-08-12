import sys
sys.stdin = open('GNS_test_input.txt')
T = int(input())
for i in range(T):
    TC = list(input().split())
    str_list = list(input().split())
    str_dic = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    # dict형으로 받아서 key*value로 출력하는걸 목표로 하자
    for num in str_list:
        str_dic[num] += 1                   # dict형에 집어넣기
    print(TC[0])                            # 문제에서 #n 형으로 주어져있기 때문에 이것을 그대로 사용함
    for j in str_dic:
        print(f'{j} '*str_dic[j], end=' ')  # dict형을 한줄에 출력하기 위해서 end 사용함
    print()                                 # 줄바꿈
