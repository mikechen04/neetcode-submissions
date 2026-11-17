class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set
        # add s[i] into the set 
        # if it is already in the set keep incrementing l while doing like set(from l:r)
        # then check again, if its unique then keep going
        # record the count
        # if the count > max_count then assign max_count to count
        l, count = 0, 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            seen.add(s[r])

            if (r-l+1) > count:
                count = r - l + 1
        
        return count