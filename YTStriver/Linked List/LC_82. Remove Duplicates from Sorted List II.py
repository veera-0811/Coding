# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
            
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head
        while curr is not None:
            if curr.next is not None and curr.val == curr.next.val:
                while curr is not None and curr.val == prev.next.val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next

'''
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
'''