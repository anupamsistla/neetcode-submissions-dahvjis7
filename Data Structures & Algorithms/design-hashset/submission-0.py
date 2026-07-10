class MyHashSet:

    def __init__(self):
        self.currSet = []

    def add(self, key: int) -> None:
        if not key in self.currSet:
            self.currSet.append(key)

    def remove(self, key: int) -> None:
        if key in self.currSet:
            self.currSet.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.currSet        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)