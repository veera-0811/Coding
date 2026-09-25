class Solution:
    def replaceDigits(self, s):
        n = len(s)
        res = ""
        i = 0
        while i < n-1:
            p = chr(ord(s[i]) + int(s[i+1]))
            res += s[i]
            res += p
            i += 2
        if i < n:
            res += s[i]
        return res

s = "a1c1e1"            #Output: "abcdef"
print(Solution().replaceDigits(s))
'''Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'    '''