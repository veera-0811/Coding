# Brute Force
def helper(arr,pages,n):
    stu = 1
    pages_of_stu = 0
    for i in range(n):
        if arr[i]+pages_of_stu <= pages:
            pages_of_stu += arr[i]
        else:
            stu += 1
            pages_of_stu = arr[i]
    return stu

def findPages(arr, n, m):
    if m > n:
        return -1
    low = max(arr)
    high = sum(arr)
    for pages in range(low,high):
        cntstudents = helper(arr,pages,n)
        if cntstudents <= m:
            return pages
        
# Optimized Solution -> Binary Search on answers(Variety - 2)
def helper(arr,pages,n):
    stu = 1
    pages_of_stu = 0
    for i in range(n):
        if arr[i]+pages_of_stu <= pages:
            pages_of_stu += arr[i]
        else:
            stu += 1
            pages_of_stu = arr[i]
    return stu
    
class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if n < k:
            return -1
        
        l,h = max(arr),sum(arr)
        while l <= h:
            mid = l + (h-l)//2
            cntstu = helper(arr,mid,n)
            if cntstu <= k:
                h = mid - 1
            else:
                l = mid + 1
        return l
    
# Example usage
arr = [10, 20, 30, 40]
k = 4
print(Solution().findPages(arr, k))  # Output: 40