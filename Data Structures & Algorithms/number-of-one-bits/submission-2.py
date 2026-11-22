class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        n = list(map(int, str(n)))
        c = 0

        print(n)
        for i in range(len(n)):
            if n[i] == 1:
                c += 1
        
        return c

        
        
         