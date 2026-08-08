#Brute Force -> Time Complexity: O(2n) and Space Complexity: O(n)
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        
        for i in range(n//2):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        return nums    

#Optimal -> Two pointers    Time Complexity: O(n) and Space Complexity: O(n)
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        posindex=0
        negindex=1
        res=[0]*n
        for i in nums:
            if i>0:
                res[posindex]=i
                posindex+=2
            else:
                res[negindex]=i
                negindex+=2
        return res
    
nums = [3,1,-2,-5,2,-4]         #Output: [3,-2,1,-5,2,-4]
print(Solution().rearrangeArray(nums))