class MinStack:
    from collections import deque
    def __init__(self):
        self.arr=deque()
        self.mini=deque()
        

    def push(self, val: int) -> None:
        if len(self.mini)==0:
            self.mini.append(val)
        else:
            self.mini.append(min(self.mini[-1],val))
        self.arr.append(val)
        

    def pop(self) -> None:
        self.mini.pop()
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
        
