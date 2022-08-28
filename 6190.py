T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    incr = []
    for i in range(N):
        for j in range(i+1, N):
            check = nums[i]*nums[j]
            check_temp = check
            temp = []
            while check_temp:
                a = check_temp % 10
                temp.append(a)
                check_temp //= 10
            flag = True
            for k in range(len(temp)-1):
                if temp[k] < temp[k+1]:
                    flag = False
                    break
            if flag:
                incr.append(check)
    ans = -1
    if incr:
        ans = max(incr)
    print(f'#{t+1} {ans}')





