# Brute Force Approach
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    ans += 1
        return ans

# Optimal Approach
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        ans = 0
        for val in d.values():
            if val > 1:
                ans += val*(val-1)//2
        return ans

nums = [1,2,3,1,1,3]                        # Output: 4
print(Solution().numIdenticalPairs(nums))  