# LINK : https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/swap-bits

t = int(input())
for _ in range(t):
    n = int(input())
    even = (n& 0x55555555) << 1
    odd =  (n& 0xAAAAAAAA) >> 1
    print(even | odd)