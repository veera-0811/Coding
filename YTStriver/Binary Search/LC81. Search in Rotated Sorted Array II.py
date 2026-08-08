class Solution(object):
    def search(self, nums, target):
        l,h = 0,len(nums)-1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return True
                
            if nums[l] == nums[mid] and nums[mid] == nums[h]:     # This condition is added to handle the case when there are duplicate elements in the array.
                l = l + 1
                h = h - 1
                continue

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
        return False
    
# Example usage:
nums = [3, 1, 2, 3, 3, 3, 3]
target = 1
print(Solution().search(nums, target))  # Output: True