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





