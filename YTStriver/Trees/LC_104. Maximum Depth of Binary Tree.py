# Level Order Traversal -> Deque
"""
| Complexity | Value    | Reason                                                                       |
| ---------- | -------- | ---------------------------------------------------------------------------- |
| Time       | O(n)     | Every node is visited exactly once.                                          |
| Space      | O(n)     | In the worst case (complete tree), the queue stores up to about `n/2` nodes. |for skewed tree, the queue will store only one node at a time, so the space complexity is O(1). |
"""

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth

# Recursive Approach        
"""Time Complexity :- Every node is visited exactly once.
Time = O(n)

Space Complexity :- The recursion stack depends on the tree height.
Balanced tree: O(log n)
Skewed tree: O(n)
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return 1 + max(leftDepth,rightDepth)

# Input: root = [3,9,20,null,null,15,7]
# Output: 3