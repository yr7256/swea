# def heap(n):
#     if tree[n//2] and tree[n] < tree[n//2]:
#         tree[n], tree[n//2] = tree[n//2], tree[n]
#         heap(n//2)
#
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     tree = [0]
#     num = 1
#     for node in lst:
#         tree.append(node)
#         heap(num)
#         num += 1
#     ans = 0
#     while N:
#         N //= 2
#         ans += tree[N]
#     print(f'#{t+1} {ans}')


def heap_push(item):
    heap.append(item)  # 완전 이진트리니까 맨끝에 +

    child = len(heap)-1
    parent = child // 2
    # 루트노드가 아니고, 위에 봤는데 더 큰 경우 계속 돎
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]  # swap
        child = parent
        parent = child // 2


def heap_pop():
    if len(heap) == 1:  # 없을때 뽑지 않는 장치
        return

    result = heap[1]
    item = heap.pop()
    heap[1] = item

    parent = 1  # 루트부터 시작하니까 1
    child = parent * 2  # 일단 왼쪽이 작다고 가정하자

    if child+1 <= len(heap)-1:  # 오른쪽 노드가 트리 안에 존재하고 +
        if heap[child] > heap[child+1]:  # 왼쪽이 더 크면 최소힙으로서는
            child += 1  # 오른쪽으로 내려가야하는게 맞음

    # 이번에는 아래로 내려가는거니까 오른쪽 노드가 존재할때까지 +
    # 최소힙 유지를 위해 필요할때까지!
    while child <= len(heap)-1 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child  # 이번에는 내려가는거니까 반대
        child = parent * 2  # 일단 이번에도 왼쪽이라고 가정해봄

        if child+1 <= len(heap)-1:  # 아까 그 로직 반복
            if heap[child] > heap[child+1]:
                child += 1

    return result


T = int(input())
for t in range(T):
    N = int(input())
    heap = ['최소힙 :']
    for i in map(int, input().split()):
        heap_push(i)
    print(heap)
