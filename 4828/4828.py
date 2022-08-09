import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    max_num = 0  # max를 갱신
    min_num = 1000000  # min을 갱신
    for i in map(int, input().split()):
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    print(f'#{t+1} {max_num-min_num}')