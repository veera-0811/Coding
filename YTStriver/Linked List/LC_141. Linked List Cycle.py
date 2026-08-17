# Floyd’s Cycle-Finding Algorithm       Time Complexity: O(N)         Space Complexity: O(1)

class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

'''
Input: head = [3,2,0,-4]
pos = 1                     Note :- This argument is not passed to the function
Output: true
'''