'''
Approach name :- Merge Sort on Linked List
More specifically :- Divide and Conquer + Fast/Slow Pointers + Two-Pointer Merge

Time Complexity :-	O(n log n)
Space Complexity :-	O(log n) recursion stack
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def merge(self,left,right):
        dummy = ListNode(-1)
        curr = dummy
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(right)

        return self.merge(left,right)

'''
Input: head = [4,2,1,3]
Output: [1,2,3,4]
'''