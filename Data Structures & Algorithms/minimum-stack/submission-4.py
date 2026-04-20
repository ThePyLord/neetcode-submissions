class MinStack:

    def __init__(self):
        self.stack = []
        self.aux_stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.aux_stack.append(val)
        else:
            top = self.stack[-1]
            if val <= self.aux_stack[-1]: 
                self.aux_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        out = self.stack.pop()
        print(f'aux length: {len(self.aux_stack)}')
        if out == self.aux_stack[-1]:
            self.aux_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.aux_stack[-1] if self.aux_stack else self.stack[-1]
