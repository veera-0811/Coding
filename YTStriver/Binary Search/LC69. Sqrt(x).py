# Through Math
def mySqrt1(x):
    if x<2:
        return x
    v=x
    while v*v>x:
        v=(v+x//v)//2
    return v

# Brute Force
def mySqrt2(x):
    i=0
    while i*i<=x:
        i+=1
    return i-1
    
#Basic Binary Search 
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        l,h = 1,x
        ans = 1
        while l <= h:
            mid = (l+h)//2
            if mid*mid <= x:
                ans = mid
                l = mid + 1
            else:
                h = mid - 1
        return ans

# Binary Search with better space complexity
def mySqrt3(x):
    if x < 2:
        return x
    l,h = 1,x//2
    while l <= h:
        mid = (l+h)//2
        if mid*mid == x:
            return mid
        elif mid*mid < x:
            l = mid + 1
        else:
            h = mid - 1
    return h
    
# Example usage:
x = 8
print(Solution().mySqrt(x))  # Output: 2