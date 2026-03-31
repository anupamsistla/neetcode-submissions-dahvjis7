# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, head1, head2) -> ListNode:
        curr1 = head1
        curr2 = head2

        res = dummy = ListNode()
        while curr1 and curr2:
            if curr1.val < curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
            elif curr2.val <= curr1.val:
                dummy.next = curr2
                curr2 = curr2.next
            dummy = dummy.next
            
        
        if curr1 and not curr2:
            dummy.next = curr1
            
            while curr1:
                dummy = dummy.next
                curr1 = curr1.next
            
        elif curr2 and not curr1:
            dummy.next = curr2
            while curr2:
                dummy = dummy.next
                curr2 = curr2.next
    
    
        return res.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # why O(N*K)

        i = 1

        res = dummy = ListNode()
        if not lists:
            return None

        # curr = lists[0]
        # while i < len(lists):
        #     dummy.next, endOfList = self.mergeTwoLists(lists[i], curr)
            
        #     curr = dummy.next
        #     dummy = endOfList
        #     i+=1

        res = lists[0]

        while i < len(lists):
            res = self.mergeTwoLists(lists[i], res)
            i+=1
        return res          

