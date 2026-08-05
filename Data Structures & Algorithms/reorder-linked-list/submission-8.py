# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        numNodes = 0
        
        curr = head

        while curr:
            numNodes += 1
            curr = curr.next

        curr = head
        tail = None
        index = 0

        while curr:
            index += 1
            if index == numNodes // 2:    
                tail = curr.next
                curr.next = None
                break
            
            curr = curr.next
        
        prev = None
        while tail:
            nextNode = tail.next
            tail.next = prev
            prev = tail
            tail = nextNode
    
        
        tail = prev
        curr = head

        while curr and tail:
            nextNode1 = curr.next
            nextNode2 = tail.next

            curr.next = tail
            curr = nextNode1
            tail.next = curr if curr else tail.next
            tail = nextNode2
        
        return