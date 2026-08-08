# BFS Approach
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root,1)])
        while q:
            node,depth = q.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                q.append([node.left,depth + 1])
            if node.right:
                q.append([node.right,depth + 1])

# Recursive Approach
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        return 1 + min(left_depth,right_depth)

# Input: root = [3,9,20,null,null,15,7]
# Output: 2