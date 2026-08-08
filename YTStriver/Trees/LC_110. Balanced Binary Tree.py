# Brute Force Approach                  Time Complexity: O(n^2)      Space Complexity: O(h), where h is the height of the tree due to the recursion stack.
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))

def check(root):
    if root is None:
        return True
    
    lh = height(root.left)
    rh = height(root.right)

    if abs(lh - rh) > 1:
        return False
    
    left = check(root.left)
    right = check(root.right)

    if not left or not right:
        return False
    
    return True

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return check(root)



# Optimized Approach                       Time Complexity: O(n)      Space Complexity: O(h), where h is the height of the tree due to the recursion stack.

"""Key Idea: 
Instead of calculating the height of the left and right subtrees separately, we can calculate the height of the tree in a single traversal.
If at any point we find that the left and right subtrees are not balanced, we can return -1 to indicate that the tree is not balanced.
Otherwise, we return the height of the tree.
"""

def height(root):
    if not root:
        return 0
    lh = height(root.left)
    if lh == -1:
        return -1
    rh = height(root.right)
    if abs(lh-rh) > 1:
        return -1
    if rh == -1:
        return -1
    return 1 + max(lh,rh)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ans = height(root)
        return ans != -1
