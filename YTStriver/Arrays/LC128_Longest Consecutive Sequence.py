# Brute Force                                               Time Complexity: O(n^2)  Space Complexity: O(1)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        def ls(arr,num):
            return num in arr
        
        if not nums:
            return 0

        longest = 1
        for i in range(len(nums)):
            x = nums[i]
            c = 1
            while ls(nums,x+1):
                x += 1
                c += 1
            longest = max(longest,c)
        return longest
    
#Better Solution                                              Time Complexity: O(nlogn)  Space Complexity: O(1)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 1
        cnt_curr = 0
        last_smaller = float('-inf')
        
        for i in range(len(nums)):
            if nums[i]-1 == last_smaller:
                cnt_curr += 1
                last_smaller = nums[i]
            elif nums[i] != last_smaller:
                cnt_curr = 1
                last_smaller = nums[i]
            longest = max(longest,cnt_curr)
        return longest

# Optimal Solution -> SET                                              Time Complexity: O(n)  Space Complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        longest = 1
        for num in s:
            if num - 1 not in s:
                x = num
                c = 1
                while x + 1 in s:
                    x += 1
                    c += 1
                longest = max(longest,c)
        return longest
    
nums1 = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))  # Output: 9