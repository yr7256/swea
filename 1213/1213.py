import sys
sys.stdin = open('test_input.txt', 'r', encoding='UTF8')

for t in range(10):                               # test case 10개
    N = int(input())                              # N번째 case
    target = input()                              # 찾아야 할 문자열
    str_list = input()                            # 전체 문자열
    count = 0                                     # target의 개수
    for i in range(len(str_list)-len(target)+1):  # str_list 개수) - (target 개수) + 1 만큼 돌아야 한다
        if str_list[i:i+len(target)] == target:   # list slicing 이용해서 target 찾아서 있다면 count += 1
            count += 1                            #
    # count = str_list.count(target)              # .count() 쓰면 한줄에 끝..
    print(f'#{t+1} {count}')                      #