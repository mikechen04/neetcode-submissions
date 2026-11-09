class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        buy = prices[0]

        for r in range(0, len(prices)):
            buy = min(buy, prices[r])
            profit = prices[r] - buy
            if profit > maxprof:
                maxprof = profit
        
        return maxprof