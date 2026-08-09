# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dm = ListNode(-1)
        dummy = dm
        p = list1
        q = list2
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                dm.next = list1
                list1 = list1.next
            else:
                dm.next = list2
                list2 = list2.next
            dm = dm.next
        if list1 is not None:
            dm.next = list1
        if list2 is not None:
            dm.next = list2
        return dummy.next

'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''