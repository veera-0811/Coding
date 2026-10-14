# Approach: Two Pointers
# Explanation: We can use two pointers to traverse the string from left to right and right to left. We maintain two counters, left and right, to count the number of opening and closing parentheses. If at any point, the number of closing parentheses exceeds the number of opening parentheses, we reset both counters. If the number of opening and closing parentheses are equal, we update the maximum length of valid parentheses found so far. and it is done in both left to right and right to left traversal to cover all cases.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        left = right = maxi = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if right > left:
                left = right = 0
            if left == right:
                maxi = max(maxi,2*left)

        left = right = 0
        for i in range(n-1,-1,-1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left > right:
                left = right = 0
            if left == right:
                maxi = max(maxi,2*left)
        return maxi

# Approach: Sliding Window
# Explanation: We can use a sliding window approach to find the longest valid parentheses substring. We maintain two pointers, left and right, to represent the current window of valid parentheses. We also maintain a counter to keep track of the number of opening and closing parentheses in the current window. If the number of closing parentheses exceeds the number of opening parentheses, we move the left pointer to the right until the window is valid again. If the number of opening and closing parentheses are equal, we update the maximum length of valid parentheses found so far.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        maxlen = 0
        
        l = depth = 0 
        for r in range(n):
            if s[r] == '(':
                depth += 1
            else:
                depth -= 1
            
            if depth < 0:
                depth = 0
                l = r + 1
            if depth == 0:
                maxlen = max(maxlen,r-l+1)

        l = n-1
        depth = 0
        for r in range(n-1,-1,-1):
            if s[r] == '(':
                depth -= 1
            else:
                depth += 1
            if depth < 0:
                depth = 0
                l = r - 1
            if depth == 0:
                maxlen = max(maxlen,l-r+1)
        return maxlen

# Approach: Stack
# Explanation: We can use a stack to keep track of the indices of the opening parentheses. We initialize the stack with -1 to handle the case when the first valid substring starts from index 0. We iterate through the string and for each character, if it is an opening parenthesis, we push its index onto the stack. If it is a closing parenthesis, we pop the top index from the stack. If the stack becomes empty after popping, we push the current index onto the stack. Otherwise, we calculate the length of the current valid substring by subtracting the current index from the top index of the stack and update the maximum length found so far.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

# Example usage:
s = "(()"
print(Solution().longestValidParentheses(s))  # Output: 2