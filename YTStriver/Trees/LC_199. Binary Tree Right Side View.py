# Queue -> Dequeue

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            n = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if i == n - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
    

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]