# Approach: Backtracking using recursion and string concatenation
class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrack(curr,open,close):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if open < n:
                backtrack(curr+'(',open+1,close)
            if close < open:
                backtrack(curr+')',open,close+1)
        backtrack("",0,0)
        return res

# # Approach: Backtracking using recursion and shared stack
class Solution:
    def generateParenthesis(self, n):
        res = []
        stack = []
        def backtrack(open,close):
            if open == close == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append('(')
                backtrack(open+1,close)
                stack.pop()
            if close < open:
                stack.append(')')
                backtrack(open,close+1)
                stack.pop()
        backtrack(0,0)
        return res

# Example usage:
n = 3
print(Solution().generateParenthesis(n))  # Output: ["((()))","(()())","(())()","()(())","()()()"]