# Hash Map Approach -> O(n) + O(n)
# Note:- This HashMap approach works because all score[i][k] values are guaranteed to be unique; otherwise, duplicate keys would overwrite previous rows.
class Solution:
    def sortTheStudents(self, score, k):
        m,n = len(score),len(score[0])
        d = {}
        for i in range(m):
            d[score[i][k]] = score[i]
        
        res = []
        for num in sorted(d,reverse = True):
            res.append(d[num])
        return res

# Selection Sort -> (No Extra Space) O(n^2)+ O(1)
class Solution:
    def sortTheStudents(self, score, k):
        n = len(score)

        for i in range(n):
            max_index = i

            for j in range(i + 1, n):
                if score[j][k] > score[max_index][k]:
                    max_index = j

            score[i], score[max_index] = score[max_index], score[i]

        return score

# Sample Input
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
print(Solution().sortTheStudents(score, k))  # Output: [[7,5,11,2],[10,6,9,1],[4,8,3,15]]