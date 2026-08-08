# LINK: https://hive.smartinterviews.in/contests/smart-interviews-basic/problems/check-bit

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,i = map(int,input().split())
if ((n>>i)&1) ==1:
    print("true")
else:
    print("false")