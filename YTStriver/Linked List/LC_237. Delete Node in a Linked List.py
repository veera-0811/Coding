'''
Question :- Delete the given node.
Note that by deleting the node, we do not mean removing it from memory. We mean:
- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
-All the values before node should be in the same order.
-All the values after node should be in the same order.
'''

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

'''
Input: head = [4,5,1,9]             # head is not given in the function
node = 5
Output: [4,1,9]
'''