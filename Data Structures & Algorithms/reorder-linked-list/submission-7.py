# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tail = slow.next
        slow.next = None
        curr1 = head
        curr2 = None

        while tail:
            nextNode = tail.next
            tail.next = curr2
            curr2 = tail
            tail = nextNode
    
        curr1 = head
        while curr2:
            nextNode1 = curr1.next
            nextNode2 = curr2.next
            curr1.next = curr2
            curr1 = nextNode1
            curr2.next = curr1
            curr2 = nextNode2
            
        
