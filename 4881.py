def arr_min(depth, temp):                         # depth는 층수, temp 는 층수들의 원소의 합
    global answer                                 #
    if temp >= answer:                            # acc가 answer 보다 더 크면 더 볼 필요가 없다
        return                                    #
    if depth == N:                                # depth가 끝까지 갔으면 최소값 갱신 시켜주기
        if answer > temp:                         #
            answer = temp                         #
        return                                    #
    for i in range(N):                            # 1층에서 0번 index 썼으면
        if not check[i]:                          # 지하에서는 못쓰게 check하고
            check[i] = 1                          # 다시 1칸 밑으로 (밑으로 내려가면서 그 층의 수는 temp에 더해주기)
            arr_min(depth+1, temp+arr[depth][i])  # -> 계속 반복하다가 끝나면
            check[i] = 0                          # 1층 초기화해주기 (다음은 1번 index 써야하니까 0번 비워줘야함) -> 이거 반복하기


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 100
    check = [0]*N
    arr_min(0, 0)
    print(f'#{t+1} {answer}')

# 다시 풀기