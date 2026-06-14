class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0,0)
        self.lenList = 0
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node: Node) -> None:
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
        
        return self.cache[key].value if key in self.cache else -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            self.cache[key].value = value
            return
        else:
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
            self.lenList += 1

            if self.lenList > self.capacity:
                toRemove = self.left.next.key
                self.remove(self.left.next)
                del self.cache[toRemove]
                self.lenList -= 1
            return