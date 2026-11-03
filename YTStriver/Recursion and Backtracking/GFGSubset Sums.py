# Approach: Backtracking            Time Complexity: O(2^n)  Space Complexity: O(n)
class Solution:
	def subsetSums(self, arr):
		n = len(arr)
		res = []
		def helper(ind, s):
			if ind >= n:
				res.append(s)
				return
			s += arr[ind]
			helper(ind + 1, s)
			s -= arr[ind]
			helper(ind + 1, s)
		helper(0, 0)
		return res

# Example Usage
arr = [5, 6, 7]               # Output: [0, 5, 6, 7, 11, 12, 13, 18]
print(Solution().subsetSums(arr))