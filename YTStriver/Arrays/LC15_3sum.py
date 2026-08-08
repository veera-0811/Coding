'Brute Force'
'Time ~ O(N^3 + NlogN) space ~ O(no. of triplets)'
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j] + nums[k] == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        res.add(tuple(temp))
        return list(list(i) for i in res)

'Better Approach'
'Using HashSet'

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = set()
        for i in range(n):
            hashset = set()
            for j in range(i+1,n):
                sum = -(nums[i]+nums[j])
                if sum in hashset:
                    temp = [nums[i],nums[j],sum]
                    temp.sort()
                    res.add(tuple(temp))
                hashset.add(nums[j])
        return list(list(i) for i in res)
    
'Optimal Approach'
'   Using Sorting and Two pointers'
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue
            j = i+1
            k = n-1
            while j<k:
                sum = nums[i]+nums[j] + nums[k]
                if sum < 0: 
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k  and nums[k] == nums[k+1]:
                        k -= 1
        return res