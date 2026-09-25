# Sliding Window
# Key Idea: Find the longest subarray with sum = totalSum - x. Then answer = n - length of that subarray.

# In detail, we can use a sliding window approach to find the longest subarray with sum = totalSum - x. We maintain a current sum and two pointers (i and j) to represent the current window. We expand the window by moving j and shrink it by moving i when the current sum exceeds the target. If we find a subarray with the desired sum, we update the maximum length found so far. Finally, if we found a valid subarray, we return n - maxlen; otherwise, we return -1.
# Why we taken totalSum - x? Because we want to remove elements from the start and end of the array to reduce x to zero. The remaining elements in the middle should sum up to totalSum - x.
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        t = sum(nums) - x
        if t == 0:
            return n
        curr_sum = maxlen = 0
        i = j = 0
        while j < n:
            curr_sum += nums[j]
            while i < n and curr_sum > t:
                curr_sum -= nums[i]
                i += 1
            if curr_sum == t:
                maxlen = max(maxlen,j-i+1)
            j += 1
            
        if maxlen == 0:
            return -1
        return n - maxlen

nums = [1,1,4,2,3]      # Output: 2
x = 5
print(Solution().minOperations(nums, x))