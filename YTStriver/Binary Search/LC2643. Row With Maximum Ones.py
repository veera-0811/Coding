# Brute Force approach
def rowAndMaximumOnes(mat):
    m = len(mat)
    n = len(mat[0])
    ind = -1
    max_cnt = -1
    for i in range(m):
        cnt = 0
        for j in range(n):
            cnt += mat[i][j]
        if cnt > max_cnt:
            max_cnt = cnt
            ind = i
    return [ind,max_cnt]

# Binary Search doesn't work since some rows are not sorted in leetcode input

#  GFG -> Row with Max 1s in Rowwise Sorted (Binary Search)         -> Better Approach
def binarysearch(arr,n,t):
    l,h = 0,n-1
    res = n
    while l <= h:
        mid = (l+h)//2
        if arr[mid] >= t:
            res = mid
            h = mid - 1
        else:
            l = mid + 1
    return res

class Solution:
    def rowWithMax1s(self, mat):
        m = len(mat)
        n = len(mat[0])
        ind = -1
        max_cnt = 0
        for i in range(m):
            cnt = n - binarysearch(mat[i],n,1)
            if cnt > max_cnt:
                max_cnt = cnt
                ind = i
        return ind
    
# GFG -> Row with Max 1s in Rowwise Sorted (Binary Search)         -> Optimal Approach
class Solution:
    def rowWithMax1s(self, arr):
        m = len(arr)
        n = len(arr[0])
        row = 0
        col = n - 1
        res = -1
        while row < m and col >= 0:
            if arr[row][col] == 1:
                col -= 1
                res = row
            elif arr[row][col] == 0:
                row += 1
        return res

# Example Usage
mat = [[0,1],[1,0]]                 #Output: [0,1]
print(rowAndMaximumOnes(mat))