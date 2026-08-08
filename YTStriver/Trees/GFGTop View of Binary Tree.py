# BFS Approach -> Level Order Traversal         Time Complexity: O(NlogN)  Space Complexity: O(N)
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
# Key Idea: # Assign each node a Horizontal Distance (HD) from the root.
# During BFS, store the first node encountered for every HD.
# The first node at each HD is the top-most visible node.
from collections import deque
class Solution:
    def topView(self, root):
        if not root:
            return []
        q = deque([(root,0)])
        mp = {}
        while q:
            node,hd = q.popleft()
            if hd not in mp:
                mp[hd] = node.data
            
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
        ans = []
        for val in sorted(mp):
            ans.append(mp[val])
        return ans

# Input: root = [10, 20, 30, 40, 60, 90, 100]
# Output: [40, 20, 10, 30, 100]