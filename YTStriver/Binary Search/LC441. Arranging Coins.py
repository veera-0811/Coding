# Approach: Using the formula for the sum of the first k natural numbers, we can derive a formula to find the maximum number of complete rows that can be formed with n coins. The sum of the first k natural numbers is given by k*(k+1)/2. We need to find the largest integer k such that k*(k+1)/2 <= n. By rearranging this inequality, we can derive a quadratic equation and solve for k using the quadratic formula. The final result is obtained by taking the floor of the solution.
'''
Concept :- O(1) Approach
1+2+3+...+x = n
-> (1+x)x/2 = n
-> x^2+x = 2n
-> x^2+x+1/4 = 2n +1/4
-> (x+1/2)^2 = 2n +1/4
-> (x+0.5) = sqrt(2n+0.25)
-> x = -0.5 + sqrt(2n+0.25)
'''
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor(-0.5 + math.sqrt(2*n+0.25))

# Brute Force Approach -> O(N) Approach
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        x = n
        crt = 0
        for i in range(1,x+1):
            n -= i
            if n >= 0:
                crt += 1
            else:
                break
        return crt

# Binary Search Approach -> O(logN) Approach
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = l + (r - l) // 2
            coins = mid * (mid + 1) // 2
            if coins == n:
                return mid
            elif coins < n:
                l = mid + 1
            else:
                r = mid - 1
        return r

# Example usage:
n = 5
print(Solution().arrangeCoins(n))  # Output: 2