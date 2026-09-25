# Binary Search Approach
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
            
        l,h = 1,num//2
        while l <= h:
            mid = (l+h)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                l = mid+1
            else:
                h = mid-1
        return False
    
# Example Usage
num = 16        #Output: true
print(Solution().isPerfectSquare(num))