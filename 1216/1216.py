for _ in range(10):                                                             # test case는 10개
    T = int(input())                                                            # test case 번호
    arr = [input() for _ in range(100)]                                         # 100*100 글자판 받기 (split()으로 받지 않기 조심!)
    zipped_arr = list(map(list, zip(*arr)))                                     # 글자판의 전치행렬
    max_num = 0                                                                 # 최댓값 저장하는 수
    for i in range(100):                                                        # arr[i][j] 에서 i
        for j in range(100):                                                    # 회문의 길이가 20이라면 [0:20]에서 [80:100]까지 가니까
            for k in range(j+1):                                                # k는 range(j+1)까지 돌아야함
                if arr[i][k:100-j+k] == arr[i][k:100-j+k][::-1]:                # 일반화 시킨다면 슬라이싱은 [k:100-j+k] 이다.
                    max_num = max(max_num, 100-j)                               # 회문의 길이는 100-j
                if zipped_arr[i][k:100-j+k] == zipped_arr[i][k:100-j+k][::-1]:  # 전치도 마찬가지
                    max_num = max(max_num, 100-j)                               # 100에서부터 점점 내려간다고 했을 때,
                if not max_num:                                                 # 0이 아닌 수가 등장할 때가 가장 큰 수이다.
                    break                                                       # 만약 길이가 99인 회문이 있다면 그 밑이 모두 회문이라도
    print(f'#{T} {max_num}')                                                    # 최댓값은 99이기 때문이다.
