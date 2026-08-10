# Brute Force Approach
def reverse(a,i,j):
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        res = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][i] = matrix[i][j]
        
        for row in res:
            reverse(row,0,n-1)

        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]

        return matrix

# Optimal Approach


matrix = [[1,2,3],[4,5,6],[7,8,9]]          # Output: [[7,4,1],[8,5,2],[9,6,3]]
print(Solution().rotate(matrix))