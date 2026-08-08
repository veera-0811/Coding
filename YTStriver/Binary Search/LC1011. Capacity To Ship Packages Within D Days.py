# Brute Force          Time Complexity: O((sum(weights) - max(weights) + 1)*n) where n is the length of weights array.
def helper(weights,cap):
    days = 1
    load = 0
    for w in weights:
        if load + w > cap:
           days += 1
           load = w 
        else:
            load += w
    return days

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        for cap in range(max(weights),sum(weights)+1):
            req_days = helper(weights,cap)
            if req_days <= days:
                return cap
            
# Binary Search          Time Complexity: O(n * log(sum - max  + 1)) where n is the length of weights array.
def helper(weights,cap):
    days = 1
    load = 0
    for w in weights:
        if load + w > cap:
           days += 1
           load = w 
        else:
            load += w
    return days

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l,h = max(weights),sum(weights)
        ans = -1
        while l <= h:
            mid = (l+h)//2
            if helper(weights,mid) <= days:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans

# Example Usage
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(Solution().shipWithinDays(weights, days))