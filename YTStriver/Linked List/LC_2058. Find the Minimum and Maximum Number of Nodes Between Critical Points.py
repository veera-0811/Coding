# Time Complexity: O(n)     Space Complexity: O(1)
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1,-1]
        prev = head
        curr = head.next

        first_idx = last_idx = -1
        idx = 1 
        min_dist = float('inf')
        check = False
        
        while curr.next:
            if curr.val < prev.val and curr.val < curr.next.val:
                check = True
            elif curr.val > prev.val and curr.val > curr.next.val:
                check = True

            if check:
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist,idx-last_idx)
                last_idx = idx

            prev = prev.next
            curr = curr.next
            idx += 1
            check = False
        
        if first_idx == last_idx:
            return [-1,-1]
        max_dist = last_idx - first_idx
        return [min_dist,max_dist]


# Example usage
# Input :- Creating a linked list: 5 -> 3 -> 1 -> 2 -> 5 -> 1 -> 2               Output: [1,3]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(5)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(2)

print(Solution().nodesBetweenCriticalPoints(head))