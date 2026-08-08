# Brute Force Approach                          Time Complexity: O(m x n)
def searchMatrix(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == target:
                return True
    return False
    
# Binary Search -> Better Approach              Time Complexity: O(m * log n)
def binarySearch(arr,n,t):
    l,h = 0,n-1
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == t:
            return True
        elif arr[mid] < t:
            l = mid + 1
        else:
            h = mid - 1
    return False

def searchMatrix(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        if matrix[i][0] <= target and target <= matrix[i][n-1]:
            return binarySearch(matrix[i],n,target)
    return False

# Binary Search -> Optimal Solution             Time Complexity: O(log(m x n)) 😍😍😍

# Key Intuition: The 2D matrix can be treated as a 1D sorted array since the last element of a row is less than the first element of the next row.
# To convert a 1D index to a 2D index, we can use the following formulas:
# row = index // n
# col = index % n

class Solution:
    def searchMatrix(self,matrix,target):
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        h = (m*n) - 1
        while l <= h:
            mid = (l+h)//2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False


# Example Usage
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]            #Output: true
target = 3
print(Solution().searchMatrix(matrix,target))