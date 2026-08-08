# Two pointers  ->  Optimal Approach
class Solution(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(s - target) < abs(closest_sum - target):
                    closest_sum = s
                if s < target:
                    j += 1
                else:
                    k -= 1
        return closest_sum
    
# Example Usage
nums = [-1,2,1,-4]                             #Output: 2 [-1,2,1])
target = 1
print(Solution().threeSumClosest(nums,target))