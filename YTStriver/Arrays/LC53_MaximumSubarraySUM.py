#Brute                                  Time Complexity: O(n³)
def maxSubArray1(nums):
    maxi = nums[0]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            curr_sum = 0
            for k in range(i, j+1):
                curr_sum += nums[k]
            maxi = max(maxi, curr_sum)
    return maxi

#Better                                 Time Complexity: O(n²)
def maxSubArray2(nums):
    maxi = nums[0]
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            maxi = max(maxi,curr_sum)
    return maxi

#Optimal -> Kadane's Algorithm          Time Complexity: O(n)
def maxSubArray(nums):
    n=len(nums)
    curr_sum=nums[0]
    max_sum=nums[0]
    for i in range(1,n):
        curr_sum=max(nums[i],curr_sum+nums[i])
        max_sum=max(curr_sum,max_sum)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]      #Output: 6
print(maxSubArray(nums))