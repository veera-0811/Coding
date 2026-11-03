# Approach: Backtracking            Time Complexity: O(2^n)  Space Complexity: O(n)
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:        
        n = len(nums)
        nums.sort()
        res = []
        def helper(ind,temp):
            if ind >= n:
                res.append(temp.copy())
                return
            temp.append(nums[ind])
            helper(ind+1,temp)
            temp.pop()
            j = ind+1
            while j < n and nums[j] == nums[ind]:
                    j += 1
            helper(j,temp)
        helper(0,[])
        return res

nums = [1,2,2]              # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(Solution().subsetsWithDup(nums))