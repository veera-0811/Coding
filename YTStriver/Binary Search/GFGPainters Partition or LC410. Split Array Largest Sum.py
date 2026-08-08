# Brute Force
def helper(arr,k,n,w):
    painters = 1
    units_painted = 0
    for i in range(n):
        if arr[i] + units_painted <= w:
            units_painted += arr[i]
        else:
            painters += 1
            units_painted = arr[i]
    return painters<=k
class Solution:
    def minTime1(self, arr, k):
        if k == 1:
            return sum(arr)
        n = len(arr)
        if k > n:
            return -1
            
        low = max(arr)
        high = sum(arr)
        for w in range(low,high):
            if helper(arr,k,n,w):
                return w

# Binary Search on answers (Variety - 2)
def helper(arr,k,n,w):
    painters = 1
    units_painted = 0
    for i in range(n):
        if arr[i] + units_painted <= w:
            units_painted += arr[i]
        else:
            painters += 1
            units_painted = arr[i]
    return painters<=k

class Solution:
    def minTime(self, arr, k):
        if k == 1:
            return sum(arr)
        n = len(arr)
        if k > n:
            return -1
            
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = low + (high-low)//2
            if helper(arr,k,n,mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
    
# Example usage
arr = [10, 20, 30, 40]
k = 2
print(Solution().minTime(arr, k))  # Output: 60