class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {} 

        while True:
            temp = 0
            for digit in str(n):
                temp += int(digit) ** 2
            
            if temp == 1:
                return True
            elif temp in seen:
                return False
        
            seen[temp] = 1
            n = temp