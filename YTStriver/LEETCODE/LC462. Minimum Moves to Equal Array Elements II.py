class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = nums[n//2]
        moves = 0
        for i in range(n):
            moves += abs(nums[i] - mid)
        return moves

# Example Usage
nums = [1,2,3]              # Output: 2
print(Solution().minMoves2(nums))