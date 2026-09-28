class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0)+1
        
        ans = 0
        odd = False
        for val in d.values():
            if val%2 == 0:
                ans += val
            else:
                odd = True
                ans += val -1

        return ans+1 if odd else ans

s = "abccccdd"          # Output: 7
'''Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.'''
u = "a"                  # Output: 1
t = "aaabbbddd"         # Output: 7
'''Explanation: One longest palindrome that can be built is "abdadba", whose length is 7.
two characters can be taken from all the three characters and one character can be taken from the remaining character.
'''

print(Solution().longestPalindrome(s))
print(Solution().longestPalindrome(u))
print(Solution().longestPalindrome(t))