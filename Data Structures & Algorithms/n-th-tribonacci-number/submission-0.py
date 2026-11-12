class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            if n != 0:
                return 1
            else:
                return 0
        
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)