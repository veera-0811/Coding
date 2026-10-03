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



'''
GFG Question: given the length of the string n, generate all valid parentheses combinations. The number of opening and closing parentheses should be equal to n/2 each.
class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrack(curr,open,close):
            if len(curr) == n:
                res.append(curr)
                return
            if open < n//2:
                backtrack(curr+'(',open+1,close)
            if close < open:
                backtrack(curr+')',open,close+1)
        backtrack("",0,0)
        return res

# Example usage:
n = 6
print(Solution().generateParenthesis(n))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
'''