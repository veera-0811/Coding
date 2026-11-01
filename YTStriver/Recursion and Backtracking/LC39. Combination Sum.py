# Approach: Recursion and Backtracking
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        ans = []
        temp = []
        def helper(ind,arr,s):
            if s == 0:
                ans.append(temp.copy())
                return
            if ind >= n or s < 0:
                return
            
            temp.append(arr[ind])
            s -= arr[ind]
            helper(ind,arr,s)
            s += arr[ind]
            temp.pop()
            helper(ind+1,arr,s)
            
        helper(0,candidates,target)
        return ans

# Same approach but with a different structure
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        ans = []
        temp = []
        def helper(ind,arr,s):
            if ind >= n:
                if s == 0:
                    ans.append(temp.copy())
                return

            if arr[ind] <= s:
                temp.append(arr[ind])
                helper(ind,arr,s - arr[ind])
                temp.pop()

            helper(ind+1,arr,s)

        helper(0,candidates,target)
        return ans

# Example usage
candidates = [2,3,6,7]              #  Output: [[2,2,3],[7]]
target = 7
print(Solution().combinationSum(candidates, target))