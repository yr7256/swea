T = int(input())                         # test case 개수
for t in range(T):                       #
    P, A, B = map(int, input().split())  # 책 페이지, A가 찾아야할 페이지, B가 찾아야할 페이지
    l_A, r_A = 1, P                      #
    l_B, r_B = 1, P                      #
    count_A = 0                          # A를 찾는데 몇번 걸렸는지 세는 수
    count_B = 0                          # B를 찾는데 몇번 걸렸는지 세는 수
    ans = ''                             # 결과값 저장
    while True:                          # A 이분탐색
        c = (l_A+r_A)//2                 # 중간값 설정 후 count+=1
        count_A += 1                     #
        if c == A:                       # 같으면 break
            break                        #
        elif c > A:                      # A가 중간값보다 적으면 오른쪽이 중간값
            r_A = c                      #
        else:                            # A가 중간값보다 크면 왼쪽이 중간값
            l_A = c                      #
    while True:                          # B 이분탐색
        c = (l_B+r_B)//2                 # 중간값 설정 후 count+=1
        count_B += 1                     #
        if c == B:                       # 같으면 break
            break                        #
        elif c > B:                      # B가 중간값보다 적으면 오른쪽이 중간값
            r_B = c                      #
        else:                            # B가 중간값보다 크면 왼쪽이 중간값
            l_B = c                      #
    if count_A < count_B:                # B가 더 크면 결과값에 A 저장
        ans = 'A'                        #
    elif count_A > count_B:              # A가 더 크면 결과값에 B 저장
        ans = 'B'                        #
    else:                                # 같으면 0
        ans = 0                          #
    print(f'#{t+1} {ans}')               #


def binary_search(book, target):
    count = 0
    left = 1
    right = book
    while left <= right:
        middle = (left+right)//2
        count += 1
        if middle == target:
            return count
        elif middle > target:
            right = middle
        else:
            left = middle


T = int(input())
for t in range(T):
    P, A, B = map(int, input().split())
    if binary_search(P, A) < binary_search(P, B):
        ans = 'A'
    elif binary_search(P, A) > binary_search(P, B):
        ans = 'B'
    else:
        ans = 0
    print(f'#{t + 1} {ans}')