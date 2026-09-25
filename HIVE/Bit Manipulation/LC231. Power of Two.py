# REcursion
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        if n%2 != 0:
            return False
        return self.isPowerOfTwo(n//2)

# Bit Manipualtion
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n>0 and n&(n-1)==0)

n = 1           # Output: true
print(Solution().isPowerOfTwo(n))