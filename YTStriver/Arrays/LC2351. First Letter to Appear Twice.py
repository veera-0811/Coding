class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
            else:
                return s[i]

# Example usage
s = "abccbaacz"          # Output: "c"
print(Solution().repeatedCharacter(s))