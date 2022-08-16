T = int(input())                          # test case 개수
for t in range(T):                        #
    N = input()                           # 찾아야할 N
    M = input()                           # 조사할 M
    dic = {}                              # N의 요소 하나씩 받을 빈 dict 생성
    for i in N:                           # dict에 N의 요소 하나씩 넣기
        dic[i] = 0                        # (dict이므로 중복된 것은 합쳐진다.)
    for j in M:                           # M의 요소에서
        try:                              # dict 안에 있다면
            dic[j] += 1                   # 요소 +=1 씩
        except KeyError:                  # 없다면 (KeyError 없어도 무방)
            continue                      # 지나가기
    print(f'#{t+1} {max(dic.values())}')  # 제일 높은 값 출력하기
