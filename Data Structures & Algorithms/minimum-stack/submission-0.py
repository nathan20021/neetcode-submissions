class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_val = []
        
    def push(self, val: int) -> None:
        self.main_stack.append(val)
        
        if len(self.min_val) == 0 or self.min_val[-1] >= val:
            self.min_val.append(val)

    def pop(self) -> None:
        if len(self.main_stack) == 0 :
            return
        val = self.main_stack.pop()
        if val == self.min_val[-1]:
            self.min_val.pop()


    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
        
# 5 3 4 6 1