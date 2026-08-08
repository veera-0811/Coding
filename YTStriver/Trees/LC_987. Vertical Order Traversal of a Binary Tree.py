# optimal

from collections import deque
import heapq
class Solution:
    def verticalTraversal(self, root):
        mp = {}
        q = deque([(root, 0, 0)])

        while q:
            node, col, row = q.popleft()

            if col not in mp:
                mp[col] = {}

            if row not in mp[col]:
                mp[col][row] = []

            heapq.heappush(mp[col][row], node.val)

            if node.left:
                q.append((node.left, col - 1, row + 1))

            if node.right:
                q.append((node.right, col + 1, row + 1))

        ans = []
        for col in sorted(mp):
            curr = []
            for row in sorted(mp[col]):
                while mp[col][row]:
                    curr.append(heapq.heappop(mp[col][row]))
            ans.append(curr)

        return ans

# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

'''
mp = {
    -1: {
        1: [2]
    },

    0: {
        0: [1],
        2: [4, 5]
    },

    1: {
        1: [3]
    }
}
'''