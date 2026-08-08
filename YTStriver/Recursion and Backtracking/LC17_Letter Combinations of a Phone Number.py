# DFS   -> Backtracking
class Solution:
    def letterCombinations(self,digits) :
        if not digits:
            return []
        phone = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        
        def backtrack(index,curr_combination):
            if  len(curr_combination) == len(digits):
                res.append(curr_combination)
                return
            curr_digit = digits[index]
            letters = phone[curr_digit]
            for letter in letters:
                backtrack(index + 1,curr_combination + letter)

        backtrack(0,"")
        return res

# Example Usage
digits = "23"               #Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(Solution().letterCombinations(digits))