class Solution:
    def minMoves(self, nums: list[int]) -> int:
        res = 0
        mini = min(nums)
        for num in nums:
            res += num - mini
        return res

nums = [1,2,3]              # Output: 3
print(Solution().minMoves(nums))

'''
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''