class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)
        
    def pop(self) -> None:
        val = self.mainStack.pop()
        if self.minStack and val == self.minStack[-1]:
            self.minStack.pop()
        return val

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
