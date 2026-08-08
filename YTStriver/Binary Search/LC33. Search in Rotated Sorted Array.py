class Solution(object):
    def search(self, nums, target):
        l,h = 0,len(nums)-1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1
    
# Example usage:
nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums, target))  # Output: 4