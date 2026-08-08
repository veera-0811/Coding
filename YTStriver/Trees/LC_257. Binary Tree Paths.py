# # DFS + Backtracking  
class Solution:

    def is_leaf(self,root):
        return root.left is None  and root.right is None
    
    def helper(self,root,res,path):
        if not root:
            return
        res.append(str(root.val))
        if self.is_leaf(root):
            path.append("->".join(res))
        else:
            self.helper(root.left,res,path)
            self.helper(root.right,res,path)

        res.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        path = []
        self.helper(root,[],path)
        return path