# Linear Search
def nthRoot(n, m):
    for i in range(1, m + 1):
        if i ** n == m:
            return i
        elif i ** n > m:
            return -1
    return -1

# Binary Search
def nthRoot(n, m):
    if m == 0:
        return m
    l,h = 1,m
    while l <= h:
        mid = (l+h)//2
        if mid**n == m:
            return mid
        elif mid**n < m:
            l = mid + 1
        else:
            h = mid - 1
    return -1

# Binary Search
''' Key Idea is
Return 1 if mid^n == m
Return 0 if mid^n < m
Return 2 if mid^n > m
'''

def func(mid, n, m):        # To calculate mid^n and compare with m
    ans = 1
    for i in range(n):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0

def NthRoot(n, m):
    low,high = 1, m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Example
n = 3
m = 27
print(NthRoot(n, m))