# Level Order Traversal
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def rightView(self, root):
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == n-1:
                    res.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res