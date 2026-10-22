# Recursion and Backtracking -> It gives ***TimeLimitExceeded(TLE)*** for large inputs. so, It is not optimised code.
def pos(ind,arr,n,temp,k,ans):
    if ind >= n:
        if sum(temp) == k:
            ans.append(temp.copy())
        return
    temp.append(arr[ind])
    pos(ind+1,arr,n,temp,k,ans)
    temp.pop()
    pos(ind+1,arr,n,temp,k,ans)

class Solution:
    def checkSubsequenceSum(self, arr, k):
        n = len(arr)
        temp = []
        ans = []
        pos(0,arr,n,temp,k,ans)
        return len(ans) > 0

