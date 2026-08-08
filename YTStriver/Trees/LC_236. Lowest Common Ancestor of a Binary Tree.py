# Brute Force Approach: DFS + Root-to-Node Path (Backtracking)       Time Complexity : O(2N + H) = O(N)  Space Complexity : O(H)
'''
DFS to find p
+
DFS to find q
+
Compare two paths

It traverses the tree twice.

It also stores two complete paths.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def find_path(self,root,target,path):
        if not root:
            return False
        
        path.append(root)
        if root == target:
            return True
        if self.find_path(root.left,target,path):
            return True
        if self.find_path(root.right,target,path):
            return True

        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        self.find_path(root,p,path1)
        self.find_path(root,q,path2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]

# Optimized Approach: Recursive DFS (Postorder)               Time Complexity : O(N)  Space Complexity : O(H)
'''
Single DFS (Postorder)
One recursive traversal.
While returning,
every node decides whether
it is the LCA.
No paths are stored.
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p == root or q == root:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root