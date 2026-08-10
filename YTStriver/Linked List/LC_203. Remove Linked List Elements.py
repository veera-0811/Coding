# 
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.val == val:
            head = head.next
            if head is None:
                return head

        curr = head
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        if head.val == val:
            return head.next
        return head

                                            # OR  Removed the unnecesary check for head.val == val at the end of the function, as it is already handled in the while loop above. which was shown below.

# Here, we are removing all the nodes from the linked list that have a specific value (val).
# The function takes the head of the linked list and the value to be removed as input and returns the modified linked list.

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        while head is not None and head.val == val:
            head = head.next

        curr = head

        while curr is not None and curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

'''
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
'''