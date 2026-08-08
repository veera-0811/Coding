class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            cost = prices[i] - mini
            profit = max(profit,cost)
            mini = min(mini,prices[i])
        return profit
    
prices = [7,1,5,3,6,4]         #Output: 5
print(Solution().maxProfit(prices))