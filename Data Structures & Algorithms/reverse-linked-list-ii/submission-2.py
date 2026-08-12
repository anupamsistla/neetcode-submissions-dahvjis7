# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode()
        dummy.next = head 
        curr = head
        index = 0

        while curr:
            if index == left-1:
                prev = None 
                nextNode = None
                tail = curr

                while curr:
                    nextNode = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nextNode
                    index += 1

                    if index == right:
                        dummy.next = prev
                        tail.next = curr
                        
                        return dummy.next if left == 1 else head
            else:
                dummy = dummy.next
            
            curr = curr.next
            index += 1
