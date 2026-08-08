# Brute Force Approach
class Solution:
    def median(self, mat):
        m = len(mat)
        n = len(mat[0])
        res = []
        for i in range(m):
            for j in range(n):
                res.append(mat[i][j])
        res.sort()
        return res[m*n //2]
    
# Binary Search Approach

def upperBound(arr, x):
    l, h = 0, len(arr) - 1
    ans = len(arr)
    while l <= h:
        mid = (l + h) // 2

        if arr[mid] > x:
            ans = mid
            h = mid - 1
        else:
            l = mid + 1

    return ans

class Solution:
    def median(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        low = matrix[0][0]
        high = matrix[0][-1]

        for i in range(R):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][C - 1])

        req = (R * C) // 2

        while low <= high:
            mid = (low + high) // 2

            count = 0
            for i in range(R):
                count += upperBound(matrix[i], mid)

            if count <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low 
        
        
# Example usage:
matrix = [[1, 3, 5], [2, 6, 9],[3, 6, 9]]
print(Solution().median(matrix))  # Output: 5