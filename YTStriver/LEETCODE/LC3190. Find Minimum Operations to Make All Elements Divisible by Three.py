class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for num in nums:
            if num%3 != 0:
                ops += 1
        return ops

# Example Usage
nums = [1,2,3,4]            # Output: 3
print(Solution().minimumOperations(nums))