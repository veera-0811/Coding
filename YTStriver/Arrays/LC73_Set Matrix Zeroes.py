#Brute Force Solution                                     Time Complexity: O(m*n*(m+n)+(m*n)) ~ powerofcube  Space Complexity: O(1)
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        
        def markrow(i):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1
        def markcol(j):
            for i in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    markrow(i)
                    markcol(j)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

#Better Solution -> Using Extra Space                      Time Complexity: O(m*n)  Space Complexity: O(m+n)
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        row = [0]*m
        col = [0]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0

# Optimal Solution -> Using Matrix Itself                      Time Complexity: O(m*n)  Space Complexity: O(1)


# Question:
'''
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[3,4,5,2],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-10^9 <= matrix[i][j] <= 10^9
'''