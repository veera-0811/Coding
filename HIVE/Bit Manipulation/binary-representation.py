# LINK : https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/binary-representation

t = int(input())
for _ in range(t):
    n = int(input())
    b = bin(n)
    print(b[2:])

# Generic Approach
t = int(input())
for _ in range(t):
    n = int(input())
    b = ""
    while n != 0:
        b = str(n%2) + b
        n = n//2
    print(b)