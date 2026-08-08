# Optimized Solution -> Binary Search     Time: O(log(max(arr) + k))         Space: O(1)
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = len(arr)
        l,h = 0,n-1
        while l <= h:
            mid = (l+h)//2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                l = mid + 1
            else:
                h = mid - 1
        return l + k

# Brute Force       Time: O(n)        Space: O(1)
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k





    
# Brute Force       Time: O(max(arr) + k)         Space: O(n + k)
class Solution:
    def findKthPositive1(self, arr: list[int], k: int) -> int:
        s = set(arr)
        res = []
        for i in range(1,max(arr)+k+1):
            if i not in s:
                res.append(i)
        return res[k-1]

# Brute Force       Time: O((max(arr) + k)*n)         Space: O(k)
class Solution:
    def findKthPositive2(self, arr: list[int], k: int) -> int:
        res = []
        for i in range(1,max(arr)+k+1):
            if i not in arr:
                res.append(i)
        return res[k-1]
    
# Example Usage
arr = [2,3,4,7,11]
k = 5
print(Solution().findKthPositive(arr, k))