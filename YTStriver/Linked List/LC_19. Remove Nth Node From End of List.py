# Key Idea: Two pointer approach, move first pointer n steps ahead and then move both pointers until first reaches the end.
# The second pointer will be at the node before the one we want to remove.

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        first = head
        second = head
        for _ in range(n):
            first = first.next

        if first is None:
            return head.next

        while first.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        
        return head

'''
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''