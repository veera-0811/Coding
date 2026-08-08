# Heap
import heapq
class Solution:
    def maxProduct(self,nums):
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        ele1 = -heapq.heappop(heap) - 1
        ele2 = -heapq.heappop(heap) - 1
        return ele1 * ele2

# Example usage:
nums = [3,4,5,2]        #Output: 12 
print(Solution().maxProduct(nums))