# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        
        first, second = head, prev

        while second:
            next1 = first.next
            next2 = second.next

            first.next = second
            first = next1
            second.next = first
            second = next2

            
