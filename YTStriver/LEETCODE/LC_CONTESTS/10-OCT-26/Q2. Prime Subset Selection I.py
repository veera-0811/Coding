import math
def seive(n):
    b = [True]*(n+1)
    b[0],b[1] = False,False
    for i in range(2,int(math.sqrt(n))+1):
        if b[i] == True:
            for j in range(i*i,n+1,i):
                b[j] = False
    res = []
    for i in range(n+1):
        if b[i]:
            res.append(i)
    return res
    
class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        prime = seive(n)
        l = maxlen = sumi = 0
        i = j = -1
        for r in range(len(prime)):
            sumi += prime[r]
            while sumi > s:
                sumi -= prime[l]
                l += 1
            size = r-l+1
            if maxlen <= size:
                i = l
                j = r
                maxlen = size
        return [] if i==-1 and j==-1 else prime[i:j+1]

'''
n = 15, s = 15

Output: [3,5,7]
'''