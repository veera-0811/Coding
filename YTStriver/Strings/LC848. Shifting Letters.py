# Approach: Prefix Sum + ASCII value
class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        n = len(s)
        sf = [0]*n
        sf[-1] = shifts[-1]
        for i in range(n-2,-1,-1):
            sf[i] = shifts[i] + sf[i+1]

        res = ""
        for i in range(n):
            val = (ord(s[i])+sf[i] - ord('a'))%26 +ord('a')
            res += chr(val)        
        return res

s = "abc"           # Output: "rpl"
shifts = [3,5,9]
print(Solution().shiftingLetters(s, shifts))