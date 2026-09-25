# Approach: Frequency Count + Sorting
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0)+1
        
        def sort_key(item):
            return item[1]
        
        arr = sorted(d.items(),key=sort_key,reverse = True)
        
        ans = ""
        for ch,freq in arr:
            ans += ch*freq
        return ans

s = "tree"              # Output: "eert"        Expected: "eetr"
print(Solution().frequencySort(s))


# Approach: Frequency Count + Sorting + ASCII value             -> Mostly Preferred Approach
class Solution:
    def frequencySort1(self, s: str) -> str:
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0)+1
        
        def sort_key(item):
            return (-item[1],item[0])
        
        arr = sorted(d.items(),key=sort_key)
        
        ans = ""
        for ch,freq in arr:
            ans += ch*freq
        return ans

s = "tree"              # Output: "eert"        Expected: "eetr"
print(Solution().frequencySort1(s))