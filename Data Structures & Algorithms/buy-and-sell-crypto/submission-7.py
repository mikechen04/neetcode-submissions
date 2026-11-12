class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxp = 0

        for r in range(len(prices)):
            buy = min(buy, prices[r])
            prices = prices[r] - buy
            if prices > maxp:
                maxp = prices
        
        return maxp