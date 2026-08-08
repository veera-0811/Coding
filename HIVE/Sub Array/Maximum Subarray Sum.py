# Link :- https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/maximum-subarray-sum

# Kadane's Algorithm
t = int(input())
for _ in range(t):
    n  = int(input())
    a = list(map(int,input().split()))
    curr_sum = max_sum = a[0]
    temp_st = st = end = 0
    for i in range(1,n):
        if a[i] > curr_sum + a[i]:
            temp_st = i
            curr_sum = a[i]
        else:
            curr_sum += a[i]
            
        if max_sum < curr_sum:
            max_sum = curr_sum
            st = temp_st
            end = i
    print(max_sum,st,end)

'''
Input
3
9
-24 0 28 28 55 -31 -27 -45 -24
10
40 5 39 45 31 -44 73 -16 -31 27
7
57 18 -14 17 31 16 -16

Output
111 1 4
189 0 6
125 0 5
'''