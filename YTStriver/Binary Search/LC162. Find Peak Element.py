# Linear Search
def findPeakElement1(nums):
    n = len(nums)
    for i in range(n):
        if (i == 0 or nums[i-1] < nums[i]) and (i == n-1 or nums[i] > nums[i+1]):
            return i

# Binary Search
class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        l,h = 0,n-1
        while l < h:
            mid = (l+h)//2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                h = mid
        return l

# Example usage:
nums = [1, 2, 3, 1]
print(findPeakElement1(nums))
print(Solution().findPeakElement(nums))  # Output: 2 (index of the peak element)


# Basic Binary Search for single peak element   (see Video for more details)
class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        l,h = 1,n-2
        while l <= h:
            mid = (l+h)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                l = mid + 1
            elif nums[mid] > nums[mid+1]:
                h = mid - 1
        return -1
    
# Basic Binary Search for multiple peak elements
class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        l,h = 1,n-2
        while l <= h:
            mid = (l+h)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                l = mid + 1
            else:
                h = mid - 1
        return -1