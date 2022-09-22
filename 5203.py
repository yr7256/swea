'''
베이비진 만드는 함수 하나 만들자.
그 다음에 쪼개서 가져가게 하고
'''


def babygin(n):
    for i in range(8):
        if n[i] >= 1 and n[i+1] >= 1 and n[i+2] >= 1:
            return True
    for j in range(10):
        if n[j] == 3:
            return True
    return False


T = int(input())
for t in range(T):
    cards = list(map(int, input().split()))
    one = {}
    two = {}
    ans = 0
    for i in range(10):
        one[i] = 0
        two[i] = 0
    for i in range(6):
        one[cards[2*i]] += 1
        if babygin(one):
            ans = 1
            break
        elif babygin(two):
            ans = 2
            break
        two[cards[2*i+1]] += 1
        if babygin(one):
            ans = 1
            break
        elif babygin(two):
            ans = 2
            break
    print(f'#{t+1} {ans}')
