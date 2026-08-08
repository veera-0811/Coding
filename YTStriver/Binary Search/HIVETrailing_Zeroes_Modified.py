# Binary Search
def trail(n):
    s = 0
    while n > 0:
        s += n//5
        n = n//5
    return s

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0:
        print(4)
        continue
    
    l = 1
    h = n * 6
    ans = -1
    while l <= h:
        mid = (l+h)//2
        if trail(mid) >= n:
            ans = mid
            h = mid - 1
        else:
            l = mid + 1
    
    if ans != -1 and trail(ans) == n:
        print(5)
    else:
        print(0)

'''
Trailing Zeros Modified bookmarkGiven an integer N, print the number of positive integers whose factorial ends with N 0's.

Input Format
The first line of input contains T - number of test cases. Its followed by T lines, each containing an integer N.

Output Format
For each test case, print the number of positive integers whose factorial ends with N 0's, separated by newline.

Constraints
30 points
1 <= T <= 100
0 <= N <= 104

70 points
1 <= T <= 1000
0 <= N <= 1014

Example
Input
3
1
5
2

Output
5
0
5

Explanation

Test Case 1:
The positive integers whose factorial ends with one 0 are: 5, 6, 7, 8, 9

Test Case 2:
There are no positive integers whose factorial ends with five 0's.

Test Case 3:
The positive integers whose factorial ends with two 0's are: 10, 11, 12, 13, 14
'''