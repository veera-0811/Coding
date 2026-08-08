# Brute Force approach
class Solution:
    def kthElement(self, a, b, k):
        merged = a + b
        merged.sort()
        return merged[k-1]

# Binary Search
class Solution:
    def kthElement(self, a, b, k):
        n1 = len(a)
        n2 = len(b)
        if n1 > n2:
            return self.kthElement(b,a,k)
        n = n1 + n2
        left = k
        low = max(0,k-n2)
        high = min(k,n1)
        while low <= high:
            mid1 = (low+high)//2
            mid2 = left - mid1
            l1 = l2 = float('-inf')
            r1 = r2 = float('inf')
            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            if mid1 - 1 >= 0:
                l1 = a[mid1-1]
            if mid2 - 1 >= 0:
                l2 = b[mid2-1]
            if l1 <= r2 and l2 <= r1:
                return max(l1,l2)
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0

# Example Usage
a = [2, 3, 6, 7, 9]                 # Output: 6
b = [1, 4, 8, 10]
k = 5
print(Solution().kthElement(a,b,k))