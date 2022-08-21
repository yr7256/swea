class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        pop_item = self.stack.pop()
        return pop_item

    def is_empty(self):
        return not self.stack


T = int(input())
for t in range(T):
    arr = Stack()
    s = input()
    ans = 1
    for i in s:
        if i == '(':
            arr.push(i)
        else:
            if arr.is_empty():
                arr.push(i)
                break
            else:
                arr.pop()
    if arr.is_empty():
        ans = 1
    else:
        ans = -1
    print(f'#{t+1} {ans}')