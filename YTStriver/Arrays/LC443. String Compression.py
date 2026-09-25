# Two Pointers Approach -> O(n) Time Complexity and O(n) Space Complexity
class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        i = j  = 0
        while i < n:
            ch = chars[i]
            c = 0
            while i < n and chars[i] == ch:
                c += 1
                i += 1
        
            chars[j] = ch
            j += 1
            if c > 1:
                for digit in str(c):
                    chars[j] = digit
                    j += 1
        return j

# Example usage
chars = ["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","d"]
print(Solution().compress(chars))  # Output: 7