# Hashmap -> O(nlogn) + O(n)
class Solution:
    def sortPeople(self,names,heights):
        n = len(names)
        d = {}
        for i in range(n):
            d[heights[i]] = names[i]
        heights.sort(reverse = True)
        ans = []
        for h in heights:
            ans.append(d[h])
        return ans

# Selection Sort -> (No Extra Space) O(n^2)+ O(1)
class Solution:
    def sortPeople(self, names, heights):
        n = len(heights)

        for i in range(n):
            max_index = i

            for j in range(i + 1, n):
                if heights[j] > heights[max_index]:
                    max_index = j

            heights[i], heights[max_index] = heights[max_index], heights[i]
            names[i], names[max_index] = names[max_index], names[i]

        return names

# Sample Input
names = ["Mary","John","Emma"]          # Output: ["John","Mary","Emma"]
heights = [180,165,170]
print(Solution().sortPeople(names, heights))