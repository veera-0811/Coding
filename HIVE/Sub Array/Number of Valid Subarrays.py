# Link:- https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/number-of-valid-subarrays

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    d = {0:1}
    s = 0
    c = 0
    for i in range(n):
        if a[i] == 1:
            s += 1
        else:
            s += -1
        if s not in d:
            d[s] = 1
        else:
            c += d[s]
            d[s] += 1
    print(c)        

'''
Input :-
3
4
1 0 1 0
10
1 0 1 0 0 1 0 0 1 1
4
1 1 1 1

Output :-
4
14
0
'''