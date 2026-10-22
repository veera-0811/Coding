# Hashmap Approach
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        
        maxlen = 0
        for num in d:
            if num+1 in d:
                maxlen = max(maxlen,d[num]+d[num+1])
        return maxlen

# Sliding Window Approach
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        maxlen = 0
        i = 0
        for j in range(i+1,n):
            while nums[j] - nums[i] > 1:
                i += 1
            if nums[j]-nums[i] == 1:
                maxlen = max(maxlen,j-i+1)
        return maxlen

nums = [1,3,2,2,5,2,3,7]                # Output: 5
print(Solution().findLHS(nums))
'''
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
'''