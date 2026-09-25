'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.
Note :-
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output 

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
'''

# Brute Force Approach
class Solution:
    def findDuplicates(self, nums):
        n = len(nums)
        res = []

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and nums[i] not in res:
                    res.append(nums[i])

        return res

# Better Approach -> Using Hashing
class Solution:
    def findDuplicates(self, nums):
        seen = set()
        res = []

        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen.add(num)

        return res

# Optimal Approach -> No Extra Space with O(n) Time Complexity
class Solution:
    def findDuplicates1(self, nums):
        n = len(nums)
        res = []
        for i in range(n):
            ind = abs(nums[i])
            if nums[ind-1] > 0:
                nums[ind-1] *= -1
            else:
                res.append(ind)
        return res

nums = [4,3,2,7,8,2,3,1]        #Output: [2,3]
print(Solution().findDuplicates1(nums))