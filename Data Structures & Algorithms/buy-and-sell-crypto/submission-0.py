class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for num in range(len(prices)):
            if prices[num] < min_price:
                min_price = prices[num]
            elif prices[num] - min_price > max_profit:
                max_profit = prices[num] - min_price
        
        return max_profit