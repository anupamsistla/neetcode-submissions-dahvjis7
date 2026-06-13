# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        index = count - n
        curr = head
        if index == 0:
            head = head.next
            curr = None
            return head
        
        else:
            count = 0
            while curr:
                if count == index - 1:
                    temp = curr.next
                    curr.next = curr.next.next
                    temp = None

                curr = curr.next
                count += 1
        
            return head


