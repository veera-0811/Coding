'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    
    def isLeaf(self,root):
        return root.left is None and root.right is None
    
    def left_boundary(self,root,res):
        curr = root
        while curr:
            if not self.isLeaf(curr):               #curr.left or curr.right:
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    
    def add_leaf(self,root,res):
        if not root:
            return
        
        if self.isLeaf(root):
            res.append(root.data)
            return
        
        self.add_leaf(root.left,res)
        self.add_leaf(root.right,res)
    
    def right_boundary(self,root,res):
        curr = root
        temp = []
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
                
        while temp:
            res.append(temp.pop())
    
    def boundaryTraversal(self, root):
        if not root:
            return []
            
        res = []
        if not self.isLeaf(root):
            res.append(root.data)
            
        self.left_boundary(root.left,res)
        self.add_leaf(root,res)
        self.right_boundary(root.right,res)
        return res
        
        
# Example usage:
# Input: root = [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N]
# Output: [1, 2, 4, 8, 9, 6, 7, 3]