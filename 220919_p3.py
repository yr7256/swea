N = int(input())
dic = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4,
       '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9}
for i in range(N):
    s = input()
    temp = bin(int(s, 16))[2:]
    ans = '0'*(len(s)*4-len(temp))+temp
    ans = ans[len(s)//2:-len(s)//2]
    print(ans)
    for i in range(0, len(ans), 6):
        print(dic[ans[i:i+6]], end=' ')
    print()
