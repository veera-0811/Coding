# Queue -> dequeue

from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans[::-1]
    
# Example Usage
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
