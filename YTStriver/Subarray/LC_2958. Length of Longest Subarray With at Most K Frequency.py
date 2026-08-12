class Solution:
    def maxSubarrayLength(self, nums, k):
        h = {}
        res = float('-inf')
        l = 0
        for r in range(len(nums)):
            num = nums[r]
            h[num] = h.get(num,0)+1
            while h[num] > k:
                h[nums[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res

nums = [1,2,3,1,2,3,1,2]                        # Output: 6
k = 2                 
print(Solution().maxSubarrayLength(nums, k))  