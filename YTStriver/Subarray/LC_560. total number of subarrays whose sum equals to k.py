# Prefix Sum + Hashing

'''Key Idea: We can use a prefix sum and a hash map to store the frequency of prefix sums.
For each element in the array, we calculate the current prefix sum and check if (current prefix sum - k) exists in the hash map.
If it does, it means there is a subarray that sums to k, and we can increment our count by the frequency of that prefix sum.
Finally, we update the hash map with the current prefix sum.'''

class Solution:
    def subarraySum(self,nums,k):
        n = len(nums)
        pf = {0:1}
        curr_sum = sub_cnt = 0
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum - k in pf:
                sub_cnt += pf[curr_sum - k]
            pf[curr_sum] = pf.get(curr_sum,0)+1
        return sub_cnt

nums = [1,2,3]    # Output: 2
k = 3
print(Solution().subarraySum(nums, k))