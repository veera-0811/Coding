# (even,odd) -> element is on right half
# (odd,even) -> element is on left  half

class Solution(object):
    def singleNonDuplicate(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
            
        l,h = 1,n - 2
        while l <= h:
            mid = (l+h)//2
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            elif (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                l = mid + 1
            else:
                h = mid - 1

# Example usage:
nums = [1,1,2,3,3,4,4,8,8]
print(Solution().singleNonDuplicate(nums))  # Output: 2