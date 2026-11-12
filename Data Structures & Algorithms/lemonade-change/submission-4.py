class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = twenty = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five >= 1:
                    five -= 1
                else:
                    return False
            elif bill == 20:
                twenty += 1
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 4:
                    five -= 4
                else:
                    return False
        
        return True