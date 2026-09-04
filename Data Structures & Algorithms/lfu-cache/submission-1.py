from collections import defaultdict
class ListNode:
    def __init__(self, key, val):
        self.freq = 1
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size  

    def pop(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.size -= 1
        return
    
    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1
        return
    
    def popLeft(self):
        if self.size == 0:
            return
        toRet = self.left.next
        self.pop(self.left.next)
        return toRet

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.nodeMap = {}
        self.listMap = defaultdict(LinkedList)
    
    def counter(self, node):
        cnt = node.freq
        self.listMap[cnt].pop(node)
    
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1
        
        node.freq += 1
        self.listMap[cnt+1].pushRight(node)
        return
        

    def get(self, key: int) -> int:
        if not key in self.nodeMap:
            return -1
        
        node = self.nodeMap[key]
        toRet = node.val
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return
        
        if self.cap == len(self.nodeMap):
            node = self.listMap[self.lfuCnt].popLeft()
            self.nodeMap.pop(node.key)

        
        newNode = ListNode(key, value)
        self.nodeMap[key] = newNode
        self.listMap[1].pushRight(newNode)
        self.lfuCnt = 1
        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)