import heapq
# Key Idea: Construct a max heap from the given array and pop k times to get the kth largest element.
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        for _ in range(k):
            ans = heapq.heappop(heap)
        return -ans

# Key Idea: Construct a min heap from the given array and pop until the size of the heap is equal to k to get the kth largest element.
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

# Sample Input
nums = [3,2,1,5,6,4]
k = 2                       #Output: 5
print(Solution().findKthLargest(nums, k))