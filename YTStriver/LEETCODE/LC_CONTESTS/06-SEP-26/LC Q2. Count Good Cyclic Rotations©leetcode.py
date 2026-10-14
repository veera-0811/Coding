class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        arr = nums + nums
        pf = [0]*(2*n)
        pf[0] = nums[0]
        for i in range(1,2*n):
            pf[i] = arr[i]+pf[i-1]
            
        ans = 0
        half = n//2
        for i in range(n):
            f_h = pf[i+half-1] - (pf[i-1] if i > 0 else 0)
            s_h = pf[i+n-1] - pf[i+half-1]
            if f_h > s_h:
                ans += 1
        return ans

nums = [1,2,3,4,5,6]            #Output: 3
print(Solution().countGoodRotations(nums))