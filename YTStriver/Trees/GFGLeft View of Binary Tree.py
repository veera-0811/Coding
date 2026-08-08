# Level Order Traversal
''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''
from collections import deque
class Solution:
    def leftView(self, root):
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == 0:
                    res.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res