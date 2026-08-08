#moving zeroes to the end of the array
#brute
arr=[78,0,2,79,0,35,91,4,0,90]
n=len(arr)
temp=[]
for i in arr:
    if i!=0:
        temp.append(i)
t=len(temp)
for i in range(t):
    arr[i]=temp[i]
for i in range(t,n):
    arr[i]=0
print(arr)

#optimal
class Solution:
    def moveZeroes(self, nums) -> None:
        j=-1
        for i in range(len(nums)):
            if nums[i]==0:
                j=i
                break
        if j==-1:
            return
        for i in range(j+1,len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums
print(Solution().moveZeroes(arr))
