T = int(input())                        #
for t in range(T):                      #
    N = int(input())//10                #
    dp = [0, 1, 3]                      #
    for i in range(3, N+1):             #
        dp.append(dp[i-1]+dp[i-2]*2)    #
    print(f'#{t+1} {dp[N]}')            #
