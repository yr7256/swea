# import sys
# sys.stdin = open('sample_input.txt')
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     cards = list(input())
#     card_count = [0]*10  # 카드의 개수 저장하는 리스트 만들기
#     for card in cards:  # 카드의 개수 저장
#         card_count[9-int(card)] += 1
#     max_num = 0  # 가장 많은 카드 숫자를 저장하는 수
#     for count in card_count:
#         if max_num < count:
#             max_num = count
#     for i in range(N):  # card_count를 돌면서 max_num인 수를 찾는다.
#         if card_count[i] == max_num:  # max_num에 도달하면 print 후 break
#             print(f'#{t+1} {9-i} {card_count[i]}')
#             break

import sys
sys.stdin = open('sample_input.txt')

dict형으로도 풀어보기.
T = int(input())
for t in range(T):
    N = int(input())
    dic = {}
    for i in list(map(int, list(input()))):
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    max_value = 0
    for v in dic.values():
        if v > max_value:
            max_value=v
    max_num = 0
    for num, value in dic.items():
        if value == max_value:
            if max_num < num:
                max_num = num
    print(f'#{t+1} {max_num} {max_value}')
