class Solution:
    def mostFrequent(self, nums,key):
        n = len(nums)
        d = {}
        for i in range(n-1):
            if nums[i] == key:
                d[nums[i+1]] = d.get(nums[i+1],0)+1
        
        ans = 0
        max_cnt = 0
        for num in d:
            if d[num] > max_cnt:
                max_cnt = d[num]
                ans = num
        return ans

# Sample Input
nums = [1,100,200,1,100]                # Output: 100
print(Solution().mostFrequent(nums, 1))