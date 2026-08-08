# Link: https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/pair-with-difference-k?page=0&pageSize=10&search=pair

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    seen = {}
    for i in range(n):
        if a[i] not in seen:
            seen[a[i]] = i
    found = False
    for i in range(n):
        val = k + a[i]
        if val in seen and seen[val] != i:
            found = True
            break
    if found:
        print("true")
    else:
        print("false")

'''
Input
2
5 60
1 20 40 100 80
10 11
12 45 52 65 21 645 234 14 575 112

Output
true
false
'''