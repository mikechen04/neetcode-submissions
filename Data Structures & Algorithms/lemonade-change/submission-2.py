class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dolla5 = 0
        dolla10 = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                dolla5 += 1
            elif bills[i] == 10:
                if dolla5 >= 1:
                    dolla5 -= 1
                    dolla10 += 1
                else:
                    return False
            elif bills[i] == 15:
                if dolla10 >= 1:
                    dolla10 -= 1
                    dolla5 += 1 #
                elif dolla5 >= 2:
                    dolla5 -= 2
                    dolla10 =+ 1 #
                else:
                    return False
            else: # if 20 dolla
                if dolla5 >= 3:
                    dolla5 -= 3
                elif dolla10 >= 1 and dolla5 >= 1:
                    dolla10 -= 1
                    dolla5 -= 1
                else:
                    return False
        
        return True


