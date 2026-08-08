class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        low,high = 0,n - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
# Example usage:
nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))  # Output: 4