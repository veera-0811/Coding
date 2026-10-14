def fib(n):
    res = [0,1]
    for i in range(n//2):
        val = res[-1]+res[-2]
        if val < n:
            res.append(val)
        else:
            break
    return res
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        res = fib(n)
        for i in range(len(res) - 2):
            if res[i]+res[i+1]+res[i+2] == n:
                return True
        return False

'''
n = 16
Output: true
'''