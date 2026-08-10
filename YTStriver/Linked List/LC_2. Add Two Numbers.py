# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        c = 0
        while l1 or l2 or c:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            tot = x + y + c
            c = tot//10
            curr.next = ListNode(tot%10)
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy.next

'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
'''