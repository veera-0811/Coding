# Brute Force           Time Complexity: O(n*m) where n is the length of nums and m is the maximum value in nums
import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        if len(nums) > threshold:
            return -1
        for i  in range(1,max(nums)+1):
            s = 0
            for num in nums:
                s += math.ceil(num/i)
            if s <= threshold:
                return i
        return -1

# Binary Search           Time Complexity: O(n * log(m)) where n is the length of nums and m is the maximum value in nums
import math
class Solution:
    def helper(self,nums,threshold,mid):
        s = 0
        for num in nums:
            s += math.ceil(num/mid)
        return s <= threshold

    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        if len(nums) > threshold:
            return -1
        l,h = 1,max(nums)
        ans = -1
        while l <= h:
            mid = (l+h)//2
            if self.helper(nums,threshold,mid):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans
    
# Example Usage
nums = [1,2,5,9]
threshold = 6
print(Solution().smallestDivisor(nums, threshold))