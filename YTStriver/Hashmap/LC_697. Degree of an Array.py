# MY Approach :- Hash Map + Frequency Counting + Linear Search for First and Last Occurrences
# Time complexity: O(n^2)       Space Complexity :- O(n)
class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        d = {}
        t = []
        f = 0
        for num in nums:
            d[num] = d.get(num,0)+1
            if d[num] > f:
                f = d[num]
                t = [num]
            elif d[num] == f:
                if num not in t:
                    t.append(num)
        
        ans = float('inf')
        for num in t:
            l = 0
            while l < n:
                if nums[l] == num:
                    break
                l += 1

            cnt = d[num] - 1
            if cnt == 0:
                return 1

            for r in range(l+1,n):
                if nums[r] == num:
                    cnt -= 1
                if cnt == 0:
                    ans = min(ans,r-l+1)
                    break
        return ans

# Optimal Approach
class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        d = {}
        first = {}
        last = {}
        for i in range(n):
            if nums[i] not in first:
                first[nums[i]] = i
            last[nums[i]] = i
            d[nums[i]] = d.get(nums[i],0)+1
        
        maxi = max(d.values())
        ans = float('inf')
        for num in d:
            if d[num] == maxi:
                ans = min(ans,last[num]-first[num]+1)
        return ans

# Example Usage :-
nums = [2,1,1,2,1,3,3,3,1,3,1,3,2]              # Output 7
print(Solution().findShortestSubArray(nums))