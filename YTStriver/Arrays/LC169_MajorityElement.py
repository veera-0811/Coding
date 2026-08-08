#Brute
def majorityElement(nums):
    for i in range(len(nums)):
        c=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                c+=1
        if c>len(nums)//2:
            return nums[i]

#Better -> Hashmap
def majorityElement1(nums):
    seen = {}
    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    for i in seen:
        if seen[i] > len(nums)//2:
            return i
        
#Optimal -> Boyer Moore's Voting Algorithm
def majorityElement(nums):
    n=len(nums)
    c=0
    for i in range(n):
        if c==0:
            c=1
            el=nums[i]
        elif nums[i]==el:
            c+=1
        else:
            c-=1

    c1=0
    for i in range(n):
        if nums[i]==el:
            c1+=1
    if c1> n//2:
        return el

nums = [2,2,1,1,1,2,2]      #Output:2
print(majorityElement1(nums))