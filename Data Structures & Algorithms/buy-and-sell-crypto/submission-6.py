class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxprofit = 0

        for r in range(len(prices)):
            buy = min(buy, prices[r])
            profit = prices[r] - buy # prices[r] = sell value
            if profit > maxprofit:
                maxprofit = profit
        
        return maxprofit