import sys
sys.stdin = open('input.txt')


for t in range(10):  # test case 10개
    N = int(input())
    boxes = list(map(int, input().split()))
    boxes_count = [0]*101  # 박스가 높이에 몇 개 있는지.
    min_num = 100  # 최소값, 최대값 갱신
    max_num = 0
    for box in boxes:
        boxes_count[box] += 1
        if box > max_num:
            max_num = box
        if box < min_num:
            min_num = box
    while N > 0:  # 박스 빼고 쌓기
        boxes_count[max_num] -= 1
        boxes_count[min_num] -= 1
        boxes_count[min_num+1] += 1
        boxes_count[max_num-1] += 1
        if boxes_count[min_num] == 0:
            min_num += 1
        if boxes_count[max_num] == 0:
            max_num -= 1
        N -= 1
    print(f'#{t+1} {max_num-min_num}')



