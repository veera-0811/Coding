class Solution:
    def uniformArray(self, nums):
        n = len(nums)
        hasOdd = False
        minOdd = float('inf')
        for num in nums:
            if num%2 == 1:
                hasOdd = True
                minOdd = min(num,minOdd)
        
        if not hasOdd:
            return True
        for num in nums:
            if num%2 == 0 and num < minOdd:
                return False
        return True

nums1 = [1,4,7]       #Output: true
print(Solution().uniformArray(nums1))
'''
Explanation:​​​​​​​​
Set nums2[0] = nums1[0] = 1.
Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.
Set nums2[2] = nums1[2] = 7.
nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.
'''