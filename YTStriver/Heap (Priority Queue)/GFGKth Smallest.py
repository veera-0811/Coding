import heapq

# Key Idea: Construct a min heap from the given array and pop k times to get the kth smallest element.
class Solution:
    def kthSmallest(self, arr, k):
        heapq.heapify(arr)
        for _ in range(k):
            ans = heapq.heappop(arr)
        return ans

# Key Idea: Construct a max heap from the given array and pop until the size of the heap is equal to k to get the kth smallest element.
class Solution:
    def kthSmallest(self, arr, k):
        heap = []
        for num in arr:
            heapq.heappush(heap,-num)
        while len(heap) > k:
            heapq.heappop(heap)
        return -heap[0]

# Sample Input
arr = [7, 10, 4, 3, 20, 15]
k = 3                       #Output: 7
print(Solution().kthSmallest(arr, k))