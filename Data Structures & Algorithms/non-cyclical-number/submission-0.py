class Solution:
    def findSumOfSquares(self, num: int) -> bool:
        total = 0

        while num > 0:
            digit = num % 10
            total += digit * digit
            num = num // 10

        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.findSumOfSquares(slow)
            fast = self.findSumOfSquares(self.findSumOfSquares(fast))

            if slow == fast:
                return slow == 1
    
    