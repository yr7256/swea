import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]          # 123 456 789 중요!! str으로 받아야함
    zipped_arr = list(map(list, zip(*arr)))                  # 147 258 369
    reversed_row_arr = [i[::-1] for i in arr]                # 321 654 987
    reversed_row_zipped_arr = [i[::-1] for i in zipped_arr]  # 741 852 963
    reversed_row_column_arr = reversed_row_arr[::-1]         # 987 654 321
    reversed_column_zipped_arr = zipped_arr[::-1]            # 369 258 147
    print(f'#{t+1}')
    for i in range(N):
        print(''.join(reversed_row_zipped_arr[i]), ''.join(reversed_row_column_arr[i]), ''.join(reversed_column_zipped_arr[i]))
        # int형은 join으로 못받으니 위에서 str으로 받아서 join으로 출력함