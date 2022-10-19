from collections import deque


def rotate(a, di):
    if di == 1:
        arr[a].appendleft(arr[a].pop())
    else:
        arr[a].append(arr[a].popleft())
    return


T = int(input())
for t in range(T):
    K = int(input())
    arr = [deque([0]*8)]+[deque(list(map(int, input().split()))) for _ in range(4)]
    for _ in range(K):
        idx, direction = map(int, input().split())
        rotate_lst = [(idx, direction)]
        temp = direction
        for i in range(idx-1, 0, -1):
            if arr[i][2] != arr[i+1][6]:
                temp *= -1
                rotate_lst.append((i, temp))
            else:
                break
        temp = direction
        for i in range(idx+1, 5):
            if arr[i-1][2] != arr[i][6]:
                temp *= -1
                rotate_lst.append((i, temp))
            else:
                break
        for i, d in rotate_lst:
            rotate(i, d)
    ans = 0
    for i in range(1, 5):
        ans += arr[i][0]*2**(i-1)
    print(f'#{t+1} {ans}')
