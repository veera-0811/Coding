class Solution:
    def findKRotation(self, arr):
        l,h = 0, len(arr) - 1
        ans = float('inf')
        index = -1
        while l <= h:
            mid = (l+h)//2
            if arr[l] <= arr[mid]:
                if arr[l] < ans:
                    index = l
                    ans = arr[l]
                l = mid + 1
            else:
                if arr[mid] < ans:
                    index = mid
                    ans = arr[mid]
                h = mid - 1
        return index
    
# Example Usage
arr = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findKRotation(arr))