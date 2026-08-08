# Approach 1: Using recursion
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

# Approach 2: Using iteration
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            p,q = stack.pop()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            stack.append((p.left,q.left))
            stack.append((p.right,q.right))
        return True






'''
1. Using deque as a Stack (DFS)

This is equivalent to your current solution.
'''
from collections import deque

class Solution:
    def isSameTree(self, p, q):
        stack = deque([(p, q)])

        while stack:
            p, q = stack.pop()      # LIFO

            if not p and not q:
                continue

            if not p or not q or p.val != q.val:
                return False

            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

        return True
#This performs Iterative DFS.

'''
2. Using deque as a Queue (BFS)
'''
from collections import deque

class Solution:
    def isSameTree(self, p, q):
        q1 = deque([(p, q)])

        while q1:
            p, q = q1.popleft()     # FIFO

            if not p and not q:
                continue

            if not p or not q or p.val != q.val:
                return False

            q1.append((p.left, q.left))
            q1.append((p.right, q.right))

        return True
#This performs Level Order Traversal (BFS).