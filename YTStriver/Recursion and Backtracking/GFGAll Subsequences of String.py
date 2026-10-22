# Approach -> Backtracking
def func(ind,s,n,temp,ans):
    if ind >= n:
        ans.append("".join(temp))
        return
    temp.append(s[ind])
    func(ind+1,s,n,temp,ans)
    temp.pop()
    func(ind+1,s,n,temp,ans)
    
class Solution:
	def powerSet(self, s):
		n = len(s)
		ans = []
		temp = []
		func(0,s,n,temp,ans)
		ans.sort()
		return ans

s = "abc"                   # Output: ["", "a", "ab", "abc", "ac", "b", "bc", "c"]
print(Solution().powerSet(s))