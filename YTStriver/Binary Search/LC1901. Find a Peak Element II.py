# Brute Force Approach                          Time Complexity: O(m x n)
def findPeakGrid(mat):
    m = len(mat)
    n = len(mat[0])

    for i in range(m):
        for j in range(n):
            up = down = left = right = float("-inf")

            if i > 0:
                up = mat[i - 1][j]
            if i < m - 1:
                down = mat[i + 1][j]
            if j > 0:
                left = mat[i][j - 1]
            if j < n - 1:
                right = mat[i][j + 1]

            if (mat[i][j] > up and
                mat[i][j] > down and
                mat[i][j] > left and
                mat[i][j] > right):
                return [i, j]

    return [-1, -1]