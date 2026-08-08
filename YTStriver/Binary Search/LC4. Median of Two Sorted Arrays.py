# Brute Force
class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        merged = []
        i = j = 0
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < n1:
            merged.append(nums1[i])
            i += 1
        while j < n2:
            merged.append(nums2[j])
            j += 1
        
        n = n1 + n2
        if n % 2 == 1:
            return merged[n//2]
        else:
            return (merged[n//2] + merged[(n//2) -1])/2

# Better Solution           -> Space is reduced
class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        
        ind2 = n//2
        ind1 = ind2 - 1
        ind1el = ind2el = -1

        i = j = 0
        cnt = 0
        while i< n1 and j < n2:
            if nums1[i] < nums2[j]:
                if cnt == ind1: ind1ele = nums1[i]
                if cnt == ind2: ind2ele = nums1[i]
                cnt += 1
                i += 1
            else:
                if cnt == ind1: ind1ele = nums2[j]
                if cnt == ind2: ind2ele = nums2[j]
                cnt += 1
                j += 1

        while i < n1:
            if cnt == ind1: ind1ele = nums1[i]
            if cnt == ind2: ind2ele = nums1[i]
            cnt += 1
            i += 1
        while j < n2:
            if cnt == ind1: ind1ele = nums2[j]
            if cnt == ind2: ind2ele = nums2[j]
            cnt += 1
            j += 1

        if n % 2 == 1:
            return ind2ele
        else:
            return (ind1ele + ind2ele) / 2


# Binary Search -> Optimal solution
class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        low,high = 0,n1
        left = (n1+n2+1)//2
        n = n1 + n2
        while low <= high:
            mid1 = (low + high)//2
            mid2 = left - mid1
            l1 = l2 = float("-inf")
            r1 = r2 = float("inf")
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            if l1 <= r2 and l2 <= r1:
                if n%2 == 1:
                    return max(l1,l2)
                return (max(l1,l2)+min(r1,r2))/2
            
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0            



nums1 = [1,3]                           #Output: 2.00000
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1,nums2))