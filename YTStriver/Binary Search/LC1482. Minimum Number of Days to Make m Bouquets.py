# Brute Force
class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1

        for i in range(min(bloomDay),max(bloomDay)+1):
            c = tot = 0
            for bloom in bloomDay:
                if bloom <= i:
                    c += 1
                else:
                    tot += c//k
                    c = 0
            tot += c//k
            if tot >= m:
                return i       

# Binary Search
class Solution:
    def helper(self,bloomDay,m,k,day):
        c = tot = 0
        for bloom in bloomDay:
            if bloom <= day:
                c += 1
            else:
                tot += c//k
                c = 0
        tot += c//k
        return tot >= m

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1

        l,h = min(bloomDay),max(bloomDay)
        ans = -1
        while l <= h:
            mid = (l+h)//2
            if self.helper(bloomDay,m,k,mid):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans
    
# Example
bloomDay = [7,7,7,7,13,11,12,7]
m = 2
k = 3
print(Solution().minDays(bloomDay,m,k))