class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxp = 0

        for r in range(len(prices)):
            buy = min(buy, prices[r])
            profit = prices[r] - buy
            if profit > maxp:
                maxp = profit
        
        return maxp