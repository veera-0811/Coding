# right rotate array by d places
class Solution:
    def rotate(self, nums,k) -> None:
        # Do not return anything, modify nums in-place instead.
        def reverse(arr,l,r):
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        n=len(nums)
        k=k%n
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)
        return nums
    
nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums,k))