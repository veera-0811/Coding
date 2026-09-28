# Approach: Hash Map
# Key Idea: Use a hash map to store the knowledge pairs and then iterate through the string to replace the keys with their corresponding values.

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)
        d = {}
        for l in knowledge:
            d[l[0]] = l[1]
        
        res = ""
        i = 0
        while i < n:
            if s[i] == '(':
                j = i+1
                while s[j] != ')':
                    j += 1
                key = s[i+1:j]
                if key in d:
                    res += d[key]
                else:
                    res += "?"
                i = j+1
            else:
                res += s[i]
                i += 1
        return res

# Example usage:
s = "(name)is(age)yearsold"                 # Output: "bobistwoyearsold"
knowledge = [["name","bob"],["age","two"]]
print(Solution().evaluate(s, knowledge))

s = "hi(name)"                              # Output: "hi?"
knowledge = [["a","b"]]
print(Solution().evaluate(s, knowledge))

s = "(a)(a)(a)aaa"                         # Output: "yesyesyesaaa"
knowledge = [["a","yes"]]
print(Solution().evaluate(s, knowledge))