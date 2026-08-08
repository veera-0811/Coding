# LINK: https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/power-of-2

t = int(input())
for _ in range(t):
    n = int(input())
    if n&(n-1) == 0:
        print("True")
    else:
        print("False")