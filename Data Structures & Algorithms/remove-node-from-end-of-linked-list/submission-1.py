# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #size of linked list - n + 1 = node to delete
        count = 0
        curr = head
        prev = None 
        
        temp = head
        size = 0
        while temp:
            size+=1
            temp = temp.next
        target = size - n
        if(target == 0):
            head = head.next
            return head
        
        while curr:
            if(count == target):
                toDelete = curr
                curr = curr.next
                prev.next = curr
                return head
            count +=1 
            prev = curr
            curr = curr.next
        
        


