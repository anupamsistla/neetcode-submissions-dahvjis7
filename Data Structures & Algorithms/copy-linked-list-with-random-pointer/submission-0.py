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
        toNext = {None:None}
        curr = head
        
        while curr:
            copy = Node(curr.val)
            toNext[curr] = copy
            curr = curr.next
        
        curr = head
        
        while curr:
            copy = toNext[curr]
            copy.next = toNext[curr.next]
            copy.random = toNext[curr.random]
            curr = curr.next
        return toNext[head]
