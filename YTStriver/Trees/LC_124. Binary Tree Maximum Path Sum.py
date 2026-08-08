# Brute Force using recursion to find the maximum path sum
class Solution:

    def helper(self,root):
        if not root:
            return 0

        left = max(0,self.helper(root.left))
        right = max(0,self.helper(root.right))
        
        return root.val + max(left,right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        current = root.val + left + right

        leftans = self.maxPathSum(root.left)
        rightans = self.maxPathSum(root.right)
        
        return max(current,leftans,rightans)


# optimal using recursion with using a list to store the maximum value
class Solution:

    def helper(self,root,maxi):
        if not root:
            return 0
        
        left = max(0,self.helper(root.left,maxi))
        right = max(0,self.helper(root.right,maxi))
        maxi[0] = max(maxi[0],left+right+root.val)
        return root.val + max(left,right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxi = [0]
        self.helper(root,maxi)
        return maxi[0]

# optimal using recursion with using a class variable to store the maximum value
class Solution:

    def helper(self,root):
        if not root:
            return 0
        
        left = max(0,self.helper(root.left))
        right = max(0,self.helper(root.right))
        self.maxi = max(self.maxi,left+right+root.val)
        return root.val + max(left,right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxi = float('-inf')
        self.helper(root)
        return self.maxi
