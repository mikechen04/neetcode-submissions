class Solution:
    def maxScore(self, s: str) -> int:
        pos = 1
        score = 0
        
        for i in range(1, len(s)):
            l = s[:i]
            r = s[i:]
            lscore = 0
            rscore = 0

            for j in range(len(l)):
                if l[j] == '0':
                    lscore += 1
                
            for j in range(len(r)):
                if r[j] == '1':
                    rscore += 1
            
            score = max(score, lscore + rscore)

        return score