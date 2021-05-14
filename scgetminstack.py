class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minstack) == 0 or x < self.minstack[-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minstack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
