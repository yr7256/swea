def rsp(a, b):                                      # 가위바위보 함수
    S = nums[a]-nums[b]                             #
    if S == -2 or S == 1 or S == 0:                 # 가위-보 일때 -2 나머지는 1 그리고 같을 때, 왼쪽이 이긴다.
        return a                                    #
    else:                                           #
        return b                                    #


def tournament(s, e):                               # 토너먼트 함수
    if s == e:                                      # s==e 라는 뜻은 한명이서 한다는 뜻이므로 s,e 아무거나 출력
        return s                                    #
    left = tournament(s, (s+e)//2)                  # 절반 나누는거 계속 반복하기 -> s==e 될 때까지
    right = tournament((s+e)//2+1, e)               # 오른쪽 브리켓에서도 마찬가지 -> s==e 될 때까지
    return rsp(left, right)                         # 그리고나서 가위바위보 하기


T = int(input())                                    #
for t in range(T):                                  #
    N = int(input())                                #
    nums = [0] + list(map(int, input().split()))    # 중요! indexerror 생기지 않게 리스트 왼쪽에 벽 만들어주기
    print(f'#{t+1} {tournament(1, N)}')





