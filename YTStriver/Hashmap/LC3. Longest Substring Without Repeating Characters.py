# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
    
# Hashmap
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in d and d[s[right]] >= left:
                left = d[s[right]] + 1
            d[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans

# Example
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))