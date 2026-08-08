# A sorted rotated array can have:    At most ONE drop
# A drop means:   nums[i]>nums[i+1]

class Solution(object):
    def check(self, nums):
        n = len(nums)
        c = 0
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                c += 1
        return c <= 1
    
# Example Usage
nums = [3, 4, 5, 1, 2]
print(Solution().check(nums))