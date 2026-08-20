# Count frequencies, create (frequency, -value) for every element, sort them, and restore the original values.
class Solution:
    def frequencySort(self, nums):
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        
        arr = []
        for num in nums:
            arr.append((d[num],-num))
        arr.sort()

        ans = []
        for cnt,neg_num in arr:
            ans.append(-neg_num)
        return ans

# Count frequencies, sort each unique number by frequency and decreasing value, then add it according to its frequency.
class Solution:
    def frequencySort(self, nums):
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        
        arr = []
        for num in d:
            arr.append((d[num],-num))
        arr.sort()

        ans = []
        for cnt,neg_num in arr:
            for _ in range(cnt):
                ans.append(-neg_num)
        return ans

# Count frequencies, sort hashmap items using a custom function, and rebuild the array according to the sorted frequency order.
def sort_key(item):
    num = item[0]
    count = item[1]
    return (count,-num)
class Solution:
    def frequencySort1(self, nums):
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        
        sorted_items = sorted(d.items(), key=sort_key)

        ans = []
        for num,cnt in sorted_items:
            for _ in range(cnt):
                ans.append(num)
        return ans

# Sample Input
nums = [1,1,2,2,2,3]                    # Output: [3,1,1,2,2,2]
print(Solution().frequencySort1(nums))