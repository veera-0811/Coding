# Approach: Backtracking            Time Complexity: O(2^n)  Space Complexity: O(n)
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        def helper(ind,temp):
            if ind >= n:
                res.append(temp.copy())
                return
            temp.append(nums[ind])
            helper(ind+1,temp)
            temp.pop()
            helper(ind+1,temp)
        helper(0,[])
        return res

# Example usage:
nums = [1,2,3]                  # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(Solution().subsets(nums))