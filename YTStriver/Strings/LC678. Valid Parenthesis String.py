class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        d = 0
        for i in range(n):
            if s[i] in '(*':
                d += 1
            else:
                d -= 1
            if d < 0:
                return False

        d = 0
        for i in range(n-1,-1,-1):
            if s[i] in ')*':
                d += 1
            else:
                d -= 1
            if d < 0:
                return False
            
        return True        

# Example usage:
s = "(*))"
print(Solution().checkValidString(s))  # Output: True

'''
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
Example 4:

Input: s = "("
Output: false
'''