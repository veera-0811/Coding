# DFS + Backtracking (Pre order Traversal)          Similar problem like this LC-257 https://leetcode.com/problems/binary-tree-paths/description/
class TreeNode:   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def helper(root,x,path):
    if root == None:
        return False
    
    path.append(root.data)

    if root.data == x:
        return True
    if helper(root.left,x,path):
        return True
    if helper(root.right,x,path):
        return True
    
    path.pop()
    return False
    
def pathInATree(root: TreeNode, x: int) -> list[int]:
    path = []
    helper(root,x,path)
    return path



'''
Sample Input 1 :
2
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
7
3 2 1 -1 -1 -1 -1
1
Sample output 1 :
1 3 7
3 1
'''