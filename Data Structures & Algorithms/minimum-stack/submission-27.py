class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_val.append(val)
        else:
            if val <= self.min_val[-1]:
                self.min_val.append(val)
            
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.min_val and self.stack[-1] == self.min_val[-1]:
                self.min_val.pop()
            self.stack.pop()

    def top(self) -> int:
        #if len(self.stack) == 0:
        #    return None
        return self.stack[-1] 

    def getMin(self) -> int:
        #if len(self.min_val) == 0:
        #    return None
        return self.min_val[-1]  