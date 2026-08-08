# Queue -> Dequeue
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        from collections import deque
        q = deque([root])
        ans = []
        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg = sum(level)/n
            ans.append(avg)
        return ans
    
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]