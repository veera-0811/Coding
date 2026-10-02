class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        res = [0]*n
        d = 0
        for i in range(n):
            if seq[i] == '(':
                d += 1
                res[i] = 0 if d%2 == 0 else 1
            elif seq[i] == ')':
                res[i] = 0 if d%2 == 0 else 1
                d -= 1
        return res

seq = "(()())"              # Output: [0,1,1,1,1,0]     or      [1, 0, 0, 0, 0, 1]
print(Solution().maxDepthAfterSplit(seq))