# Dummy Node + Two-Pointer approach.        Time: O(n) — each node is visited once.     Space: O(1) — only a few pointers are used; no extra data structure.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while prev.next is not None and prev.next.next is not None:
            first = prev.next
            second = prev.next.next

            next_pair = second.next

            second.next = first
            first.next = next_pair
            prev.next = second

            prev = first
        return dummy.next

'''
Input: head = [1,2,3,4]

Output: [2,1,4,3]
'''