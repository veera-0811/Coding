'''
Question :
You are given an integer array nums.

You start with an empty array ans. Repeat the following operation until nums is empty:

Identify all distinct values currently present in nums.
Remove one occurrence of every distinct value currently in nums, and append those values to ans in ascending order.
Return the array ans.
'''

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        arr = sorted(d)
        ans = []
        while d:
            for num in arr:
                if num in d:
                    ans.append(num)
                    d[num] -= 1
                    if d[num] == 0:
                        del d[num]
        return ans

# Example usage
nums = [3,1,3,2,1,3]            # Output: [1,2,3,1,3,3]
print(Solution().rearrangeArray(nums))

'''
Explanation:

Operation	Appended to ans	    nums after	ans after
1	        1, 2, 3	            [3, 1, 3]	[1, 2, 3]
2	        1, 3	            [3]	        [1, 2, 3, 1, 3]
3	        3	                []	        [1, 2, 3, 1, 3, 3]
nums is now empty, so the answer is [1, 2, 3, 1, 3, 3].©leetcode
'''