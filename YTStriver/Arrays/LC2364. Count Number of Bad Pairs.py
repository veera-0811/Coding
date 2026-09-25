# Brute Force Approach              Time Complexity: O(n^2)  Space Complexity: O(1)
class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if j-i != nums[j]-nums[i]:
                    ans += 1
        return ans

# HashMap Approach              Time Complexity: O(n)  Space Complexity: O(n)
class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        ans = 0
        mp = {}
        for i in range(n):
            diff = nums[i]-i
            if diff in mp:
                ans += mp[diff]
                mp[diff] += 1
            else:
                mp[diff] = 1
        return (n*(n-1))//2 - ans

# Example usage
nums = [4,1,3,3]
print(Solution().countBadPairs(nums))  # Output: 5

'''
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
'''