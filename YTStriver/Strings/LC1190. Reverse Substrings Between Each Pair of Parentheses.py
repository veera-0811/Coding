# It was a good and minblowing problem to solve. I have solved it using two different approaches. The first one is using a stack and the second one is using index jumping method.

# Approach : Using Stack                        # Time Complexity : O(n^2)           Space Complexity : O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == ')':
                curr = []
                while st and st[-1] != '(':
                    curr.append(st.pop())
                st.pop()
                st.extend(curr)
            else:
                st.append(ch)
        
        return ''.join(st)

# Optimal -> Index Jumping Method               # Time Complexity : O(n)            Space Complexity : O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        pair = {}
        st = []
        for i,ch in enumerate(s):
            if ch == '(':
                st.append(i)
            elif ch == ')':
                j = st.pop()
                pair[i] = j
                pair[j] = i

        i = 0
        direction = 1
        res = []
        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction
        
        return ''.join(res)

# Example Usage
s = "(u(love)i)"            #Output: "iloveu"
print(Solution().reverseParentheses(s))