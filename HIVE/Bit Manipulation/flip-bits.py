# LINK: https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/flip-bits

t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    a = m^n
    
    c = 0
    while a != 0:
        if a&1 == 1:
            c += 1
        a = a>>1
    print(c)


# Another Approach: use & to get last bit and check it another number last bit is 1 or not. 
# If it is 1 then increment the counter and right shift the number by 1. 
# Repeat this process until the number becomes 0.