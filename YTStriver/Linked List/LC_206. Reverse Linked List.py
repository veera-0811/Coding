# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        return prev

'''
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''