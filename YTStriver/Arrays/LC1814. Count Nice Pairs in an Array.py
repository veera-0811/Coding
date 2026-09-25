# Brute Force Approach          Time Complexity: O(n^2)  Space Complexity: O(1)
def rev(n):
    return int(str(n)[::-1])

class Solution:
    def countNicePairs(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+rev(nums[j]) == nums[j]+rev(nums[i]):
                    ans += 1
        return ans

# HashMap Approach              Time Complexity: O(n)  Space Complexity: O(n)
def rev(n):
    return int(str(n)[::-1])

class Solution:
    def countNicePairs(self, nums):
        n = len(nums)
        d = {}
        MOD = 10**9 +7
        ans = 0
        for i in range(n):
            diff = nums[i] - rev(nums[i])
            if diff in d:
                ans += d[diff]
                d[diff] += 1
            else:
                d[diff] = 1
        return ans%MOD

# Example usage
nums = [42,11,1,97]
print(Solution().countNicePairs(nums))  # Output: 2

'''
Explanation: The pair (0, 3) is a nice pair since 42 + rev(97) == 97 + rev(42), 42 + 79 == 97 + 24, 121 == 121.
The pair (1, 2) is a nice pair since 11 + rev(1) == 1 + rev(11), 11 + 1 == 1 + 11, 12 == 12.
There are a total of 2 nice pairs, so we return 2.
'''