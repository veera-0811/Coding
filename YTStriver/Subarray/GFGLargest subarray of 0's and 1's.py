# Brute Force
class Solution:
    def maxLen(self, arr):
        n = len(arr)
        c = 0
        for i in range(n):
            one = z = 0
            for j in range(i,n):
                if arr[j] == 0:
                    z += 1
                else:
                    one += 1
                if z == one:
                    c = max(c,j-i+1)
        return c
    
# Hashmap
class Solution:
    def maxLen(self, arr):
        n = len(arr)
        seen = {0:-1}
        c = 0
        sumi = 0
        for i in range(n):
            if arr[i] == 1:
                sumi += arr[i]
            else:
                sumi += -1
            if sumi not in seen:
                seen[sumi] = i
            else:
                l = i - seen[sumi]
                c = max(c,l)
        return c
    
# Example usage
arr = [1, 0, 1, 1, 1, 0, 0]          #Output: 6
print(Solution().maxLen(arr))