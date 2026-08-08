# Brute Force
def canweplace(arr,dist,cows):
    cntcows = 1
    last = arr[0]
    for i in range(1,len(arr)):
        if arr[i]-last >= dist:
            cntcows += 1
            last = arr[i]
        if cntcows >= cows:
            return True
    return False

class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        for i in range(1,max(stalls)-min(stalls)+1):
            if canweplace(stalls,i,k) == True:
                continue
            else:
                return i-1
            
# Optimized Solution -> Binary Search on answers(Variety - 2)
def canweplace(arr,dist,cows):
    cntcows = 1
    last = arr[0]
    for i in range(1,len(arr)):
        if arr[i]-last >= dist:
            cntcows += 1
            last = arr[i]
        if cntcows >= cows:
            return True
    return False

class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n = len(stalls)
        l,h = 1,stalls[n-1]-stalls[0]
        while l <= h:
            mid = l + (h-l)//2
            if canweplace(stalls,mid,k):
                l = mid + 1
            else:
                h = mid - 1
        return h
    
# Example usage
stalls = [1, 2, 4, 8, 9]
k = 3
print(Solution().aggressiveCows(stalls, k))  # Output: 3