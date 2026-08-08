# Brute Force
import math
class Solution:
    def minEatingSpeed(self, piles, h):
        max_pile = max(piles)
        for k in range(1, max_pile + 1):
            tot_hrs = 0
            for pile in piles:
                tot_hrs += math.ceil(pile / k)
            if tot_hrs <= h:
                return k
        return max_pile
    
# Binary Search                         Time Complexity: O(n log(max(piles)))
import math
class Solution:
    def minEatingSpeed(self, piles, h):
        low,high = 1,max(piles)
        while low <= high:
            mid = (low+high)//2
            tot_hrs = 0
            for pile in piles:
                tot_hrs += math.ceil(pile/mid)
            if tot_hrs <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low