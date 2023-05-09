class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window optimized
        table = {}
        left = right = 0
        maxval = 0
        length = len(s)
        for right in range(length):
            if s[right] in table:
                left = max(table[s[right]]+1, left)
                
            maxval = max(maxval, right-left+1)    
            table[s[right]] = right
        
        return maxval
        
        