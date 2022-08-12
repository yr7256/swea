T = int(input())                                              # test case 개수
for t in range(T):                                            #
    N = int(input())                                          # 방을 이동하는 횟수
    room = [0]*200                                            # 1이든 2든 똑같다 그러므로 방은 200개만 있어도 됨
    for i in range(N):                                        #
        start, end = map(int, input().split())                # 시작과 끝을 지정
        if start <= end:                                      # 시작보다 끝이 크거나 같을 때
            for number in range((start-1)//2, (end-1)//2+1):  #
                room[number] += 1                             #
        else:                                                 # 시작보다 끝이 작을 때
            for number in range((end-1)//2, (start-1)//2+1):  #
                room[number] += 1                             #
    print(f'#{t+1} {max(room)}')                              # 겹친 최대값을 출력