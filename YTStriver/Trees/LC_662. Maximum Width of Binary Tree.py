# Level Order Traversal (BFS) + Complete Binary Tree Indexing
# Time Complexity : O(N)  Space Complexity : O(N)

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = deque([(root,0)])
        while q:
            n = len(q)
            minimum = q[0][1]
            first = last = 0
            for i in range(n):
                node,index = q.popleft()
                curr_ind = index - minimum

                if i == 0:
                    first = curr_ind
                if i == n-1:
                    last = curr_ind
                
                if node.left:
                    q.append((node.left,2*curr_ind+1))
                if node.right:
                    q.append((node.right,2*curr_ind+2))
            ans = max(ans,last-first+1)
        return ans
                