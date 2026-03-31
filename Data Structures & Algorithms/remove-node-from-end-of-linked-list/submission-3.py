# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        length = 0

        while curr:
            length += 1
            curr = curr.next

        index = length - n

        prev = None
        count = 0
        curr = head
        if index == 0:
            nextNode = curr.next
            curr = None
            head = nextNode
            return head

        while curr.next:
            if count == index:
                nextNode = curr.next
                prev.next = nextNode
                curr = None
                return head
                # do som
            prev = curr
            curr = curr.next
            count += 1
        
        nextNode = curr.next
        prev.next = nextNode
        curr = None
        return head