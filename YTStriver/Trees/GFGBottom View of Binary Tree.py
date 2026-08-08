# BFS Approach -> Level Order Traversal         Time Complexity: O(NlogN)  Space Complexity: O(N)
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
# Key Idea: # Assign each node a Horizontal Distance (HD) from the root.
# During BFS, keep updating the value for every HD.
# Since BFS visits nodes level by level, the last node stored for each HD
# is the bottom-most visible node.
from collections import deque
class Solution:
    def bottomView(self, root):
        if not root:
            return []
        q = deque([(root,0)])
        mp = {}
        while q:
            node,hd = q.popleft()
            if not hd in mp:
                mp[hd] = [node.data]
            else:
                mp[hd].append(node.data)
            
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
            
        ans = []
        for val in sorted(mp):
            ans.append(mp[val].pop())
        return ans
                                                # OR
# BFS Approach -> Level Order Traversal         Time Complexity: O(NlogN)  Space Complexity: O(N)
# # Key Idea:
# Use BFS with Horizontal Distance (HD).
# Overwrite the node value for every HD.
# The last node encountered at each HD forms the Bottom View
from collections import deque
class Solution:
    def bottomView(self, root):
        if not root:
            return []
        q = deque([(root,0)])
        mp = {}
        while q:
            node,hd = q.popleft()
            if not hd in mp:
                mp[hd] = node.data
            else:
                mp[hd] = node.data
            
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
            
        ans = []
        for val in sorted(mp):
            ans.append(mp[val])
        return ans