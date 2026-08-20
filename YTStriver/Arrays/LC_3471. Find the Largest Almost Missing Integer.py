# Sliding window + count array + boolean array
class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = [0]*51
        for i in range(n-k+1):
            b = [False]*51
            for j in range(i,i+k):
                b[nums[j]] = True
            for m in range(51):
                if b[m]:
                    count[m] += 1
        
        for i in range(50,-1,-1):
            if count[i] == 1:
                return i
        return -1

# Sliding window + set + hashmap
class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        h = {}
        for i in range(n-k+1):
            seen = set()
            for j in range(i,i+k):
                seen.add(nums[j])
            for num in seen:
                h[num] = h.get(num,0)+1
        
        ans = -1
        for num in h:
            if h[num] == 1:
                ans = max(ans,num)
        return ans

# Sample Input
nums = [3,9,2,1,7]
k = 3
print(Solution().largestInteger(nums, k))  # Output: 7