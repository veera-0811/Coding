# Using Recursion
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n%4 != 0:
            return False
        return self.isPowerOfFour(n//4)

    # Using Bit Manipulation
    ''' A power of 4 has:
    1. n > 0
    2. Exactly one set bit → n & (n - 1) == 0
    3. That set bit must be at an even position'''

    def isPowerOfFour1(self, n: int) -> bool:
        return (n>0 and (n&(n-1))==0 and (n&0x55555555)!=0)

# Example usage
n = 16
print(Solution().isPowerOfFour1(n))  # Output: True