import sys
sys.stdin = open('input.txt')
for t in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(100):
        table = 0
        for j in range(100):
            if arr[j][i] == 1:
                table = 1
            elif arr[j][i] == 2 and table == 1:
                table = 0
                count += 1
    print(f'#{t+1} {count}')

'''
위에 N, 밑에 S 있으니까 테이블 위부터 조사해서
위에 N 있으면 밑으로 내려가다가 중간에 S 있으면 부딪히잖아
그러면 count+=1 하고 다시 처음부터 조사
'''