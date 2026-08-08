class Solution(object):                         # Binary Search -> Lower Bound
    def searchInsert(self, nums, target):
        n = len(nums)
        low,high = 0,n - 1
        res = n
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
    
# Example usage:
nums = [1,3,5,6]
nums1 = [1,3,4,6]
target = 5
print(Solution().searchInsert(nums, target))  # Output: 2
print(Solution().searchInsert(nums1, target))  # Output: 3
