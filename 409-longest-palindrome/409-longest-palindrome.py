class Solution:
    def longestPalindrome(self, s: str) -> int:
        table_set = set()
        for i in s:
            if i not in table_set:
                table_set.add(i)
            else:
                table_set.remove(i)
                
        if len(table_set) > 0:
            length = len(s) - len(table_set) + 1
        else: 
            length = len(s)
        return length