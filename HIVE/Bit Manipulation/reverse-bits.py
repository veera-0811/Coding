# LINK: https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/reverse-bits

t = int(input())
for _ in range(t):
    n = int(input())
    b = bin(n)
    new = b[2:].zfill(32)
    r = new[::-1]
    print(int(r,2))

# optimal
import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]*32
    c = -1
    while n != 0:
        rem = n % 2
        c += 1
        if rem == 1:
            a[c] = rem
        n = n//2
    
    res = 0
    p = 31
    for i in range(len(a)):
        res += a[i]*(int(math.pow(2,p)))
        p -= 1
    print(res)