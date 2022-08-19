'''
1 1 1 0 1
1 0 1 1 1
1 1 1 1 1
count 0으로 놓고
count += lst[i][j] 했다가
if count M 이면 검사
맞으면 ans +=1 아니면 count = 0 초기화
그냥 돌아서 count = M 이면 ans += 1
'''


def check(lst, M):
    ans = 0
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i][j] == 0:
                if count == M:
                    ans += 1
                count = 0
            else:
                count += 1
        if count == M:
            ans += 1
    return ans


import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    zipped_arr = list(map(list, zip(*arr)))
    print(f'#{t+1} {check(arr, M)+check(zipped_arr, M)}')
