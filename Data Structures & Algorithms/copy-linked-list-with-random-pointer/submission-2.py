"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        newHead = dummy

        curr = head
        nodes = {}
        while curr:
            if curr and curr not in nodes:
                nodes[curr] = Node(curr.val)
            
            if curr.next and curr.next not in nodes:
                nodes[curr.next] = Node(curr.next.val)
            
            if curr.random and curr.random not in nodes:
                nodes[curr.random] = Node(curr.random.val)
            
            newNode = nodes[curr]
            newNode.next = nodes[curr.next] if curr.next in nodes else None
            newNode.random = nodes[curr.random] if curr.random in nodes else None
            dummy.next = newNode
            newNode = newNode.next
            curr = curr.next
            dummy = dummy.next
        
        return newHead.next
