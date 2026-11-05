class Solution:
    
# Approach: Backtracking            Time Complexity: O(n!*n)  Space Complexity: O(n)
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        boolean = [False]*n
        temp = []
        res = []
        
        def helper(nums,temp,boolean,res):
            if len(temp) == n:
                res.append(temp.copy())
                return
            for i in range(n):
                if not boolean[i]:
                    temp.append(nums[i])
                    boolean[i] = True
                    helper(nums,temp,boolean,res)
                    temp.pop()
                    boolean[i] = False

        helper(nums,temp,boolean,res)
        return res

# Optimal: You can also use the swapping method to generate permutations without using extra space for a boolean array. Here's an alternative implementation:
# Time Complexity: O(n!*n)  Space Complexity: O(n)
    def permute1(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        
        def helper(ind,nums,res):
            if ind == n:
                temp = []                           # Simply write res.append(nums.copy()) instead of creating a new list and appending elements one by one.
                for i in range(n):
                    temp.append(nums[i])
                res.append(temp)
                return
                
            for i in range(ind,n):
                nums[i],nums[ind] = nums[ind],nums[i]
                helper(ind+1,nums,res)
                nums[i],nums[ind] = nums[ind],nums[i]

        helper(0,nums,res)
        return res

# Example usage:
nums = [1, 2, 3]                            # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permute(nums))