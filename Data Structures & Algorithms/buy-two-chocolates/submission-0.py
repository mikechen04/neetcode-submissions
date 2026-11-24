class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort(reverse=True)
        choco = prices[-1] + prices[-2]
        print(prices[-1], prices[-2])

        if money - choco >= 0:
            return money - choco
        else:
            return money