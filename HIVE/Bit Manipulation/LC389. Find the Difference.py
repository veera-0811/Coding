# Better Approach -> Hashing
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = Counter(s)
        d2 = Counter(t)
        for ch in d2:
            if ch not in d1 or d1[ch]!=d2[ch]:
                return ch

# Optimal Approach -> Bit Manipulation
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for ch in s+t:
            ans ^= ord(ch)
        return chr(ans)

# Example usage
s = "abcd"
t = "abcde"
print(Solution().findTheDifference(s, t))  # Output: "e"