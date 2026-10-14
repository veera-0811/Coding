# Approach: Hashmap
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        d = {}
        n1,n2 = len(list1),len(list2)
        i = 0
        while i < n1:
            d[list1[i]] = i
            i += 1

        res = []
        min_sum = float('inf')
        for i in range(n2):
            if list2[i] in d:
                curr_sum = i+d[list2[i]]

                if curr_sum < min_sum:
                    min_sum = curr_sum
                    res = [list2[i]]
                elif curr_sum == min_sum:
                    res.append(list2[i])
        return res

list1 = ["happy","sad","good"]              # Output: ["sad","happy"]
list2 = ["sad","happy","good"]
print(Solution().findRestaurant(list1, list2))

'''
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".
'''