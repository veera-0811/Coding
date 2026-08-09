# Tree Traversal using BFS (Level Order Traversal) with a Depth Array
from collections import deque
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)
        adj = []
        for i in range(n):
            adj.append([])
        for i in range(1,n):
            adj[parent[i]].append(i)

        depth = [0]*n
        depth[0] = 1
        h = 1
        q = deque([0])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                for child in adj[node]:
                    depth[child] = depth[node] + 1
                    h = max(h,depth[child])
                    q.append(child)

        res = 0
        for i in range(n):
            res += nums[i] * (h-depth[i]+1)
        return res


'''
return  sum of (nums[i] * (h - d + 1)) of every node

Input: parent = [-1,0,0,0,2,2], nums = [5,2,3,1,4,6]

Output: 37

Explanation:

The height of the tree is 3.

Node	nums[i]	Depth (d)	Weight
0	5	1	5 * (3 - 1 + 1) = 15
1	2	2	2 * (3 - 2 + 1) = 4
2	3	2	3 * (3 - 2 + 1) = 6
3	1	2	1 * (3 - 2 + 1) = 2
4	4	3	4 * (3 - 3 + 1) = 4
5	6	3	6 * (3 - 3 + 1) = 6
The sum of all node weights is 15 + 4 + 6 + 2 + 4 + 6 = 37.©leetcode
'''