class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize set
        chars = set()
        # initialize left pointer
        l = 0
        max_chars = 0

        for r in s:
            if r in chars:
                # if its a repeat character, get the length and record that, then reset set then continue
                if len(chars) > max_chars: # update only if its bigger than current max
                    max_chars = len(chars)
                chars.clear()
                chars.add(r)
            else:
                # add current char to set
                chars.add(r)
            # sliding window bring l forward
            l += 1
        
        # if there are no duplicates then return the len of the string
        if max_chars == 0:
            return len(s)
        else:
            return max_chars
            
        