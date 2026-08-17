# The approach name is "Two Pointer Technique" or "Pointer Switching Technique".
# The idea is to use two pointers to traverse the linked lists. When one pointer reaches the end of its list, it switches to the head of the other list.
# This way, both pointers will traverse the same number of nodes and will meet at the intersection point if there is one.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1 is not None:
                p1 = p1.next
            else:
                p1 = headB
            if p2 is not None:
                p2 = p2.next
            else:
                p2 = headA
        return p1                       # OR return p2, since both will be equal at the intersection point or None if there is no intersection.

'''
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
'''