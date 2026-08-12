# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Key Ideas: 
# 1. Use fast and slow pointers to find the middle of the linked list.
# 2. Reverse the second half of the linked list.
# 3. Compare the first half with the reversed second half to check for palindrome.

class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True

'''
Input: head = [1,2,2,1]
Output: true
'''