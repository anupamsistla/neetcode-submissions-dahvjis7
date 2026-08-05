from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

        for _ in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        
        return

    def pop(self) -> int:
        if self.stack:
            return self.stack.popleft()
        return -1

    def top(self) -> int:
        if self.stack:
            return self.stack[0]
        return -1

    def empty(self) -> bool:
        return False if self.stack else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()