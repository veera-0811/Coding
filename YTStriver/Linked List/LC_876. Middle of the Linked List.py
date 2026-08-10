# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

'''
sample Input: head = [1,2,3,4,5]
Output: [3,4,5]
sample Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
'''