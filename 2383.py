from itertools import product
from collections import deque


def dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def lunch(group, target):
    times = []
    for p in group:
        times.append(dist(p, target))
    times.sort()
    times = deque(times)
    time = 0  # 누적 시간
    stair_time = arr[target[0]][target[1]]
    end = deque([])
    while times:
        time += 1
        for _ in range(len(end)):
            if end and end[0] == time:
                end.popleft()
        while times[0] < time and len(end) < 3:
            times.popleft()
            end.append(time+stair_time)
            if not times:
                time += stair_time
                break
    return time


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stair = []
    ans = 5000
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people.append((i, j))
            if arr[i][j] > 1:
                stair.append((i, j))
    # print(list(product((0, 1), repeat=len(people))))
    for case in list(product((0, 1), repeat=len(people))):  # 깜빡깜빡
        first, second = [], []
        for i in range(len(people)):
            if case[i]:
                second.append(people[i])
            else:
                first.append(people[i])
        # print(lunch(first, stair[0]))
        # print(lunch(second, stair[1]))
        # print(first, second)
        ans = min(ans, max(lunch(first, stair[0]), lunch(second, stair[1])))
    print(f'#{t+1} {ans}')
    # print(people)
    # print(stair)
