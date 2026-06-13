# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        dummy = ListNode()
        newHead = dummy

        carry = 0
        while curr1 and curr2:
            res = curr1.val + curr2.val + carry
            carry = res//10 if res >= 10 else 0
            value = res - 10 if res >= 10 else res

            dummy.next = ListNode(value)
            dummy = dummy.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        if curr1 and not curr2: 
            while curr1:
                res = curr1.val + carry
                carry = res//10 if res >= 10 else 0
                value = res - 10 if res >= 10 else res

                dummy.next = ListNode(value)
                dummy = dummy.next
                curr1 = curr1.next

        elif curr2 and not curr1: 
            while curr2:
                res = curr2.val + carry
                carry = res//10 if res >= 10 else 0
                value = res - 10 if res >= 10 else res

                dummy.next = ListNode(value)
                dummy = dummy.next
                curr2 = curr2.next
        
        if carry:
            dummy.next = ListNode(carry)
        
        return newHead.next


