# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 3
        # 4 5 6

        # case-2
        # carry integer

    
        curr1 = l1
        length1 = 0
        curr2 = l2
        length2 = 0
        carry = 0

        while curr1:
            length1 +=1
            curr1 = curr1.next
    
        while curr2:
            length2 += 1
            curr2 = curr2.next

        if length1 < length2:
            tmp = l1
            l1 = l2
            l2 = tmp
        
        curr1, curr2 = l1, l2
        slow = None
        while curr1 and curr2:
            sumNode = curr1.val + curr2.val + carry
            if sumNode >= 10:
                carry = sumNode//10
                # this is problematic
                curr1.val = sumNode % 10
            else:
                curr1.val = sumNode
                carry = 0
            slow = curr1
            curr1 = curr1.next
            curr2 = curr2.next
        
        # slow = None
        
        if curr1:
            while curr1:
                sumNode = curr1.val + carry
                if sumNode >= 10:
                    carry = sumNode//10
                    # this is problematic
                    curr1.val = sumNode % 10
                else:
                    curr1.val = sumNode
                    carry = 0
                slow = curr1
                curr1 = curr1.next
        
        if slow == None:
            print('Hi')
        if carry != 0 and slow:
            # print("Hi")
            slow.next = ListNode(carry)
        
        

        return l1




