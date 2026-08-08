# Linear Search                             Time Complexity: O(n)
class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        first = last = -1
        for i in range(n):
            if nums[i] == target:
                if first == -1:
                    first = i
                last =i 
        return [first,last]
    
#Binary Search                              Time Complexity: O(log n) for each of the two binary searches, resulting in O(log n) overall.

# First occurrence (lower bound) and last occurrence (upper bound - 1) of the target in the sorted array.

class Solution(object):
    def searchRange1(self, nums, target):
        n = len(nums)
        def lowerBound(arr,n,x):
            low,high = 0,n - 1
            res = n
            while low <= high:
                mid = (low+high)//2
                if arr[mid] >= x:
                    res = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return res

        def upperBound(arr,n,x):
            low,high = 0,n - 1
            res = n
            while low <= high:
                mid = (low+high)//2
                if arr[mid] > x:
                    res = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return res

        lb = lowerBound(nums,n,target)
        if lb == n or nums[lb] != target:
            return [-1,-1]
        return [lb,upperBound(nums,n,target) - 1]

# Basic Binary Search                             Time Complexity: O(log n)
class Solution(object):
    def searchRange2(self, nums, target):
        n = len(nums)        
        def fun(nums,target,n):
            low,high = 0,n-1
            first = -1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def fun1(nums,target,n):
            low,high = 0,n-1
            last = -1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        f = fun(nums,target,n)
        if f == -1:                 # If the first occurrence is not found, it means the target is not present in the array, so we can directly return [-1, -1] without performing the second binary search for the last occurrence.
            return [-1,-1]
        l = fun1(nums,target,n)
        return [f,l]

# Example usage:
nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange2(nums, target))  # Output: [3, 4]