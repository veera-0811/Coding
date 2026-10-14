# Approach :- Brute Force
def sod(n,sum):
    s = 0
    while n > 0:
        d = n%10
        s += d
        n //= 10
    return s==sum

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        min_digit = 1 if num==1 else 10**(num-1)
        max_digit = 10**(num)
        res = 0
        for i in range(min_digit,max_digit):
            if sod(i,sum):
                if res < i:
                    res = i
        return "" if res==0 else str(res)

# Optimal -> Greedy Approach
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:            # It is better to write it ->    # if sum > 9*num or (sum == 0 and num > 1): return ""
            return ""

        res = ""
        for i in range(num):
            dig = min(9,sum)
            res += str(dig)
            sum -= dig
        return res

# Example Usage
num = 2                 # Output: "98"
sum = 17
print(Solution().maxSumOfSquares(num, sum))