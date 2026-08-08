# Iterative BFS -> Queue
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q=deque([(root.left,root.right)])
        while q:
            node1,node2=q.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val!=node2.val:
                return False
            q.append((node1.left,node2.right))
            q.append((node1.right,node2.left))
        return True
            

# Recursion
class Solution:

    def helper(self,node1,node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
        return self.helper(node1.left,node2.right) and self.helper(node1.right,node2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left,root.right)