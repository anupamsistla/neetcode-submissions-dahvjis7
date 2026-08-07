class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            return 1
        
        else:
            count = 1
            for i in range(len(self.stack)-1, -1, -1):
                if price >= self.stack[i]:
                    count += 1
                else:
                    self.stack.append(price)
                    return count

            self.stack.append(price)
            return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)