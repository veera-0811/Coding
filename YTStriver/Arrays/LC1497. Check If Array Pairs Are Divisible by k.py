# Approach: Remainder + Frequency Array              Time :- O(n+k)    Space :- O(k)
class Solution:
    def canArrange(self, arr, k):
        freq = [0]*k
        for x in arr:
            r = ((x % k) + k) % k
            freq[r] += 1
        
        if freq[0]%2 != 0:
            return False
        for r in range(1,k):
            if freq[r] != freq[k-r]:
                return False
        return True

# Approach: Remainder + HashMap                      Time :- O(n)      Space :- O(k) {worst case}
class Solution:
    def canArrange(self, arr, k):
        d = {}
        for num in arr:
            r = num % k
            d[r] = d.get(r,0)+1
        
        for r in d:
            if r == 0:
                if d[r]%2 != 0:
                    return False
            else:
                if d[r] != d.get(k-r,0):
                    return False
        return True


# Example usage
arr = [1,2,3,4,5,10,6,7,8,9]          # Output: True
k = 5
print(Solution().canArrange(arr, k))
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).