# Queue -> Dequeue
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []
        l = 0
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if l % 2 == 1:
                level = level[::-1]
            ans.append(level)
            l += 1
        return ans
    
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]