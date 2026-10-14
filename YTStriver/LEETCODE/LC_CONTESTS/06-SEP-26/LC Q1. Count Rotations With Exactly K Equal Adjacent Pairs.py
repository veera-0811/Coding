class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            rot = s[i:] + s[:i]
            sc = 0
            for j in range(n-1):
                if rot[j] == rot[j+1]:
                    sc += 1
            if sc == k:
                res += 1
        return res

s = "aab"
k = 1               #Output: 2
print(Solution().countRotations(s, k))