# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr1, curr2 = head, head.next

        if not curr2:
            return False

        while curr2.next and curr2.next.next:
            if curr1 == curr2:
                return True
            
            curr1 = curr1.next
            curr2 = curr2.next.next

        return False
