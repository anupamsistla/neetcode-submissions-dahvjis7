class MyHashMap:

    def __init__(self):
        self.keys = [False]*1000001
        self.vals = [-1]*1000001      

    def put(self, key: int, value: int) -> None:
        self.keys[key] = True
        self.vals[key] = value

    def get(self, key: int) -> int:
        return self.vals[key]
        
    def remove(self, key: int) -> None:
        self.keys[key] = False
        self.vals[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)