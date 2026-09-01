class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0)+1
        
        for ch in order:
            if ch in d:
                for _ in range(d[ch]):
                    res += ch
                del d[ch]
        
        for ch in d:
            for _ in range(d[ch]):
                res += ch
        return res

# Sample Input
order = "kqep"
s = "pekeq"
print(Solution().customSortString(order, s))  # Output: "kqeep"