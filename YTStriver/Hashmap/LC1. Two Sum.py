class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i,num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num],i]
            seen[num]=i
        return []
    
# Example
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums,target))