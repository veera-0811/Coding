class Solution(object):
    def findMin(self, nums):
        l,h = 0,len(nums) - 1
        while l < h:
            mid = (l+h)//2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        return nums[l]
    
#               OR
class Solution:
    def findMin(self, arr):
        l,h = 0,len(arr) - 1
        ans = float('inf')
        while l <= h:
            mid = (l+h)//2
            if arr[l] <= arr[mid]:
                ans = min(ans,arr[l])
                l = mid + 1
            else:
                ans = min(ans,arr[mid])
                h = mid - 1
        return ans

# Example Usage
nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findMin(nums))