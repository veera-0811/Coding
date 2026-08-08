# Link :- https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/maximum-contiguous-subsequence

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int,input().split()))
    arr = list(set(a))
    arr.sort()
    ans = 1
    c = 1
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1] + 1:
            c += 1
            ans = max(ans,c)
        else:
            c = 1
    print(ans)

'''
Input :-
3
8
21 -22 -22 5 -31 -24 5 -23
10
18 -33 31 33 30 -14 32 30 16 17
6
6 3 8 5 2 5

Output :-
3
4
2

Explanation :-

Test Case-1:
Subsequence is: -22, -24, -23.

Test Case-2: 
Subsequence is: 31, 33, 30, 32.

Test Case-3: 
Subsequence is: 6, 5 or 3, 2.
'''