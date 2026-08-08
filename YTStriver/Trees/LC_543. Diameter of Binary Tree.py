# Brute Force Approach          Time Complexity: O(n^2)  Space Complexity: O(h)

def height(root):
    if not root:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh,rh)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        lh = height(root.left)
        rh = height(root.right)
        current = lh + rh

        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        return max(left,right,current)

# Optimized Approach                Time Complexity: O(n)  Space Complexity: O(h)

# using class variable to store diameter as it can be updated in recursive calls.
class Solution:

    def height(self,root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        self.diameter = max(self.diameter,lh+rh)
        return 1 + max(lh,rh)    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0
            
        self.height(root)
        return self.diameter


# using list to store diameter as list is mutable and can be updated in recursive calls.
# we should not use integer(diameter = 0) as it is immutable and will not be updated in recursive calls.
def height(root,diameter):
    if not root:
        return 0
    lh = height(root.left,diameter)
    rh = height(root.right,diameter)
    diameter[0] = max(diameter[0],lh+rh)
    return 1 + max(lh,rh)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diameter = [0]
        height(root,diameter)
        return diameter[0]