"""
110                                       count = 0
121 210                                   count = 1
210 133 310                               count = 3
133 310 221 410                           count = 4
310 221 410 146 510                       count = 7
221 410 146 510 321 610                   count = 8
410 146 510 321 610 233 710               count = 9
146 510 321 610 233 710 421 810           count = 10
510 321 610 233 710 421 810 1510 910      count = 14
321 610 233 710 421 810 1510 910 521 1010 count = 15
610 233 710 421 810 1510 910 521 1010 433 count = 17
233 710 421 810 1510 910 521 1010 433 721 count = 18
끝! 마지막 받은 사람 2
"""


from collections import deque
first = 1  # 처음 줄 설 사람
queue = deque([])
N = 20
count = 0
people = 0
while count < N:
    queue.append((first, 1, 0))                     # 가장 처음 1 1 0 넣고 계속 돌리기
    people, current, acc = queue.popleft()          # 받을 사람 번호, 받을 사탕 수, 누적 수
    count += current                                # 받을 사탕만큼 count에 저장시키기
    queue.append((people, current+1, acc+current))  # 받았으면 사탕수+1 하고 누적은 받은 사탕수만큼 더해주기
    first += 1                                      # 사탕을 받으면 받을 수록 사람 수가 늘어난다 (처음엔 1명이지만 1번 받으면 2명
print(people)                                       # 2번 받으면 2명, 3번 받으면 3명...)
