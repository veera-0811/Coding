# Here, Idea is to find the first occurence and last occurrence of the target element in the sorted array using binary search. 
# The count of occurrences can be calculated as (last occurrence index - first occurrence index + 1).
# If the target element is not found, we return 0.

class Solution:
    def countFreq(self, arr, target):
        n = len(arr)
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

        f = fun(arr,target,n)
        if f == -1:
            return 0
        l = fun1(arr,target,n)
        return l - f + 1
# Example usage:
arr = [1, 2, 2, 3, 4, 4, 4, 5]
target = 4
print(Solution().countFreq(arr, target))  # Output: 3   