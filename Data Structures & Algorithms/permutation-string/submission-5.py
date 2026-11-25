class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freqs1 = {}
        l, n = 0, len(s1)

        for char in s1:
            if char in freqs1:
                freqs1[char] += 1
            else:
                freqs1[char] = 1

        for r in range(n-1, len(s2)):
            freqs2 = {}
            # add the current window to a hashmap
            # then compare it against to the s1 hashmap
            # if theyre equal, return True, else outside of the loop return False?

            for char in s2[l:r+1]:
                if char in freqs2:
                    freqs2[char] += 1
                else:
                    freqs2[char] = 1

            print(freqs1, freqs2)
            if freqs1 == freqs2:
                return True

            l += 1

        return False



