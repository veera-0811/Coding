class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        temp = []
        def helper(ind,arr,temp,s):
            if s == target:
                ans.append(temp.copy())
                return
            if ind >= n or s > target:
                return
            temp.append(arr[ind])
            s += arr[ind]
            helper(ind+1,arr,temp,s)
            s -= arr[ind]
            temp.pop()
            j = ind + 1
            while j < n and arr[j] == arr[ind]:
                j += 1
            helper(j,arr,temp,s)
        
        helper(0,candidates,temp,0)
        return ans

candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates, target))
'''Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]'''