class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        pf = {0:-1}
        curr_sum = maxlen = 0
        for i in range(n):
            curr_sum += arr[i]
            if curr_sum - k in pf:
                maxlen = max(maxlen,i-pf[curr_sum-k])
            if curr_sum not in pf:
                pf[curr_sum] = i
        return maxlen
    
# Example usage
arr = [10, 5, 2, 7, 1, -10]     # Output: 6
k = 15
print(Solution().longestSubarray(arr, k))