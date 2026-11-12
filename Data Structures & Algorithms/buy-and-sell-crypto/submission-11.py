class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxp = 0

        for r in range(len(prices)-1):
            buy = min(buy, prices[r])
            profit = prices[r] - buy
            maxp = max(maxp, profit)

        return maxp