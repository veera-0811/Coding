# LINK: https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/count-set-bits

t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    while n != 0:
        if n&1 == 1:
            c += 1
        n = n >> 1
    print(c)