N = int(input())
for i in range(N):
    s = input()
    for j in range(0, len(s), 7):
        print(int(s[j:j+7], 2), end=' ')
    print()

# T = int(input())
#
# for _ in range(T):
#     arr = input()
#     binary = []
#     ans = []
#     for i in range(0, len(arr), 7):
#         binary.append(arr[i:i+7])
#
#     for i in range(len(binary)):
#         decimal = 0
#         for j in range(7):
#             if binary[i][j] == '1':
#                 decimal += 2 ** (6-j)
#         ans.append(decimal)
#
#     print(*ans)