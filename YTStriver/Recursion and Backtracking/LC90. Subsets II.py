class Solution:
    
# Approach: Backtracking            Time Complexity: O(2^n)  Space Complexity: O(n)

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

# Approach: Backtracking using For Loop           Time Complexity: O(2^n)*O(n)  Space Complexity: O(n)

    def subsetsWithDup1(self, nums: list[int]) -> list[list[int]]:        
        n = len(nums)
        nums.sort()
        res = []
        def helper(ind,temp):
            res.append(temp.copy())
            for i in range(ind,n):
                 if i > ind and nums[i] == nums[i-1]:continue
                 temp.append(nums[i])
                 helper(i+1,temp)
                 temp.pop()
        helper(0,[])
        return res

nums = [1,2,2]              # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(Solution().subsetsWithDup1(nums))