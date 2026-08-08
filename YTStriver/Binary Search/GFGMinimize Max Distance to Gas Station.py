# Brute Force
def minMaxDist1(stations, k):
    n = len(stations)
    howMany = [0] * (n - 1)

    for _ in range(k):
        maxSection = -1.0
        maxInd = -1

        for i in range(n - 1):
            diff = stations[i + 1] - stations[i]
            sectionLength = diff / (howMany[i] + 1)

            if sectionLength > maxSection:
                maxSection = sectionLength
                maxInd = i

        howMany[maxInd] += 1

    maxAns = -1.0

    for i in range(n - 1):
        diff = stations[i + 1] - stations[i]
        sectionLength = diff / (howMany[i] + 1)
        maxAns = max(maxAns, sectionLength)

    return maxAns

# Max Heap (Priority Queue)     -> Better Solution
import heapq
from turtle import left
class Solution:
    def minMaxDist(self, stations, k):
        n = len(stations)
        
        if n <= 1:
            return 0.0
            
        howMany = [0]*(n-1)
        pq = []
        for i in range(n-1):
            diff = stations[i+1] - stations[i]
            heapq.heappush(pq,(-diff,i))
            
        for _ in range(k):
            neg_len,ind = heapq.heappop(pq)
            howMany[ind] += 1
            
            diff = stations[ind+1] - stations[ind]
            new_len = diff/(howMany[ind] + 1)
            heapq.heappush(pq,(-new_len,ind))
            
        return -pq[0][0]
    
# Binary Search     -> Optimal Solution
class Solution:
    def minMaxDist(self, stations, k):
        n = len(stations)
        
        if n <= 1:
            return 0.0
            
        low = 0.0
        high = stations[-1] - stations[0]
        
        while high - low > 1e-6:
            mid = (low + high) / 2.0
            count = 0
            
            for i in range(n - 1):
                diff = stations[i + 1] - stations[i]
                count += int(diff / mid)
                
            if count > k:
                low = mid
            else:
                high = mid
                
        return high

# Example Usage
stations = [1,13,17,23]
k = 5
print(Solution().minMaxDist(stations, k))  # Output: 3.0