def powerset(i, N, target):
    global answer
    if i == N:
        s = 0
        for i in range(N):
            if bit[i]:
                s += A[i]
        if s == target:
            # answer += 1
            temp = []
            answer.append(temp)
            for i in range(N):
                if bit[i]:
                    temp.append(A[i])
            #         print(A[i], end=' ')
            # print()
    else:
        bit[i] = 1
        powerset(i+1, N, target)
        bit[i] = 0
        powerset(i+1, N, target)


A = list({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
bit = [0]*10
answer = []
powerset(0, 10, 10)
print(answer)
# 14번째 줄으로 출력하면 리스트로 출력
# 14번째 줄과 마지막 print(answer)를 주석 처리하고
# 15,16번째 줄으로 출력하면 한 줄씩 출력됨
