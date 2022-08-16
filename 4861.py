# S='GOFFAKWFSM'
# print(S[0:5])
# print(S[5:10][::-1])
# S='NQLMHYUMBOCSZWIOBINM'
# print(S[0:6])
# print(S[7:13])

T = int(input())                                                    # test case 개수
for t in range(T):                                                  #
    N, M = map(int, input().split())                                # N*N 배열에서 길이가 M인 회문 찾기
    arr = [input() for _ in range(N)]                               # N*N 배열 받기
    zipped_arr = list(map(list, zip(*arr)))                         # arr의 전치행렬
    temp = ''                                                       # 회문 받을 temp
    # if M % 2:                                                     # 홀짝 케이스 나누고 절반 확인하기
    #     for i in range(N):
    #         for j in range(N-M+1):
    #             if arr[i][j:j+M//2] == arr[i][j+M//2+1:j+M][::-1]:
    #                 temp = arr[i][j:j+M]
    #                 break
    #             if zipped_arr[i][j:j+M//2] == zipped_arr[i][j+M//2+1:j+M][::-1]:
    #                 temp = ''.join(zipped_arr[i][j:j+M])
    #                 break
    # else:
    #     for i in range(N):
    #         for j in range(N-M+1):
    #             if arr[i][j:j+M//2] == arr[i][j+M//2:j+M][::-1]:
    #                 temp = arr[i][j:j+M]
    #                 break
    #             if zipped_arr[i][j:j+M//2] == zipped_arr[i][j+M//2:j+M][::-1]:
    #                 temp = ''.join(zipped_arr[i][j:j+M])
    #                 break
    for i in range(N):                                              #
        for j in range(N-M+1):                                      # index 조심! 만약 N=20, M=13 이라면,
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:                # [0:13]에서 [7:20]까지니까 N-M+1이어야함.
                temp = arr[i][j:j+M]                                # 그 사이에 회문 있다면 저장하고 break
                break                                               #
            if zipped_arr[i][j:j+M] == zipped_arr[i][j:j+M][::-1]:  # 전치에서도 마찬가지로 회문 있다면 저장하고 break
                temp = ''.join(zipped_arr[i][j:j+M])                #
                break                                               #
    print(f'#{t+1} {temp}')                                         #

