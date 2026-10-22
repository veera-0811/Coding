# Brute Force Approach
class Solution:
    def sumCounts(self, nums):
        n = len(nums)
        res = 0
        for i in range(n):
            d = 0
            s = set()
            for j in range(i,n):
                if nums[j] not in s:
                    d += 1
                s.add(nums[j])
                res += d*d
        return res

# Example Usage
nums = [1,2,1]          # Output: 15
print(Solution().sumCounts(nums))
'''
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
'''