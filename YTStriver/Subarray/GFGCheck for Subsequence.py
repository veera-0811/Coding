# Approach -> Two Pointers
class Solution:
    def isSubSeq(self, s1, s2):
        i = j = 0
        n1,n2 = len(s1),len(s2)
        while i < n1 and j < n2:
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == n1

# Approach -> Recursion
def func(ind1,ind2,s1,s2,n1,n2):
    if ind1 == n1:
        return True
    if ind2 == n2:
        return False
    if s1[ind1] == s2[ind2]:
        return func(ind1+1,ind2+1,s1,s2,n1,n2)
    else:
        return func(ind1,ind2+1,s1,s2,n1,n2)

s1 = "AXY"
s2 = "YADXCP"
print(Solution().isSubSeq(s1,s2))  # Output: False

s1 = "gksrek"
s2 = "geeksforgeeks"
print(Solution().isSubSeq(s1,s2))  # Output: True