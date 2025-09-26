class MinStack:

    def __init__(self) -> None:
        self.stack = []      # main stack
        self.minstack = []   # stack to track minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If minstack is empty, or val is smaller, push the new minimum
        if not self.minstack:
            self.minstack.append(val)
        else:
            current_min = self.minstack[-1]
            self.minstack.append(min(val, current_min))

    def pop(self) -> None:
        if not self.stack:
            raise Exception("Stack is empty")
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        if not self.stack:
            raise Exception("Stack is empty")
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack:
            raise Exception("Stack is empty")
        return self.minstack[-1]
