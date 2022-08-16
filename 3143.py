T = int(input())               # test case 개수
for t in range(T):             #
    A, B = input().split()     # B는 길이가 어떻든 한번에 출력되므로 길이가 1인 것과 똑같다.
    A = A.replace(B, '*')      # A에 있는 B를 길이가 1인 아무 문자열로 바꿔줌
    print(f'#{t+1} {len(A)}')  # 바꾼 뒤 길이 세기
