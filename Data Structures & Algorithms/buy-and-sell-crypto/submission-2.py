class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            buy = min(prices[:i+1])
            profit = prices[i] - buy
            maxProfit = max(profit, maxProfit)
        
        return maxProfit