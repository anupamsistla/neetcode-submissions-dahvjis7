class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxCnt = 0
        self.stacks = {}
        

    def push(self, val: int) -> None:
        valCnt = 1 + self.count.get(val, 0)
        self.count[val] = valCnt

        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stacks[valCnt] = []
        
        self.stacks[valCnt].append(val)
        return

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.count[res] -= 1

        if self.stacks[self.maxCnt] == []:
            self.maxCnt -= 1
        
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()